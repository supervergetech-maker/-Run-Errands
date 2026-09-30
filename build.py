import base64, io, re, urllib.parse, segno, pathlib

HERE = pathlib.Path(__file__).parent
PHONE = "2349068072310"          # +234 906 807 2310
WA_SHORT = "https://wa.link/kp78yr"   # decoded from the QR printed on the client's flyers

def wa(text):
    return "https://wa.me/" + PHONE + "?text=" + urllib.parse.quote(text)

GREETING = "Hi RUN ERRANDS \n\nI have an errand I'd like you to handle."
MESSAGES = {
    "{{WA_BASE}}":    GREETING,
    "{{WA_GROCERY}}": "Hi RUN ERRANDS \n\nI'd like help with grocery & personal shopping.\nWhat I need:\nMy location:\nWhen I need it:",
    "{{WA_PARCEL}}":  "Hi RUN ERRANDS \n\nI need a parcel picked up and delivered.\nPickup point:\nTracking / collection code:\nDeliver to:",
    "{{WA_PHARMACY}}":"Hi RUN ERRANDS \n\nI need a pharmacy pickup.\nPrescription / items:\nPharmacy and location:\nDeliver to:",
    "{{WA_LAUNDRY}}": "Hi RUN ERRANDS \n\nI need my laundry collected and returned.\nPickup address:\nLaundry contact:\nReturn to:",
    "{{WA_DOCS}}":    "Hi RUN ERRANDS \n\nI need a document picked up and delivered.\nWhat is being picked up:\nPickup point:\nDeliver to:",
    "{{WA_OTHER}}":   "Hi RUN ERRANDS \n\nI need help with a personal errand or purchase.\nWhat I need:\nWhere:\nWhen:",
}

def b64(p): return base64.b64encode((HERE / p).read_bytes()).decode()

# WhatsApp QR -> inline SVG (same destination as the client's printed QR)
buf = io.BytesIO()
segno.make(WA_SHORT, error="m").save(buf, kind="svg", scale=10, border=2, dark="#0A1E33", light="#FFFFFF")
(HERE / "assets/wa-qr.svg").write_bytes(buf.getvalue())
qr = "data:image/svg+xml;base64," + base64.b64encode(buf.getvalue()).decode()

html = (HERE / "template.html").read_text()
repl = {ph: wa(msg) for ph, msg in MESSAGES.items()}
repl.update({
    "{{FONT_400}}": b64("assets/fonts/poppins-400.woff2"),
    "{{FONT_500}}": b64("assets/fonts/poppins-500.woff2"),
    "{{FONT_600}}": b64("assets/fonts/poppins-600.woff2"),
    "{{FONT_700}}": b64("assets/fonts/poppins-700.woff2"),
    "{{FONT_800}}": b64("assets/fonts/poppins-800.woff2"),
    "{{MARK_TILE_B64}}": b64("assets/mark-tile.png"),
    "{{CART_B64}}": b64("assets/cart.jpg"),
    "{{SERVICE_GROCERY_B64}}": b64("assets/service-grocery.jpg"),
    "{{SERVICE_PARCEL_B64}}": b64("assets/service-parcel.jpg"),
    "{{SERVICE_PHARMACY_B64}}": b64("assets/service-pharmacy.jpg"),
    "{{SERVICE_LAUNDRY_B64}}": b64("assets/service-laundry.jpg"),
    "{{SERVICE_DOCUMENTS_B64}}": b64("assets/service-documents.jpg"),
    "{{SERVICE_ERRANDS_B64}}": b64("assets/service-errands.jpg"),
    "{{QR_DATA_URI}}": qr,
})
# wrap section headings so they can mask up on arrival
html = re.sub(r'<h2>(?!<span)(.*?)</h2>',
              lambda m: '<h2><span class="ml"><span>' + m.group(1) + '</span></span></h2>',
              html, flags=re.S)

for k, v in repl.items():
    assert k in html, "missing placeholder: " + k
    html = html.replace(k, v)
assert "{{" not in html, "unreplaced token"
(HERE / "index.html").write_text(html)
print("built index.html", round(len(html) / 1024, 1), "KB")
print("   whatsapp links:", len(set(re.findall(r'href="(https://wa\.me/[^"]+)"', html))),
      "| masked headings:", html.count('class="ml"'),
      "| stacks:", html.count('class="stack"') + html.count(' stack"'),
      "| parallax layers:", html.count('data-par='))

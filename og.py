from playwright.sync_api import sync_playwright
import pathlib
import os
base="file://"+os.path.join(os.path.dirname(os.path.abspath(__file__)),"og-card.html")
sizes={
  # name: (viewport, css vars, outfile)
  "og-cover":     ((1200,630),  "--w:1200px;--h:630px;--pad:56px;--logo:64px;--brand:34px;--h1:96px;--sub:25px;--chip:21px;--foot:23px;--sw:620px", "runerrands/assets/og-cover.png"),
  "status-1080":  ((1080,1920), "--w:1080px;--h:1920px;--pad:78px;--logo:96px;--brand:50px;--h1:150px;--sub:39px;--chip:33px;--foot:36px;--sw:900px", "runerrands/assets/status-1080x1920.png"),
  "flyer-1080":  ((1080,1350), "--w:1080px;--h:1350px;--pad:72px;--logo:84px;--brand:44px;--h1:132px;--sub:34px;--chip:29px;--foot:31px;--sw:800px", "runerrands/assets/poster-1080x1350.png"),
}
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,(vp,vars_,out) in sizes.items():
        pg=b.new_page(viewport={"width":vp[0],"height":vp[1]})
        pg.goto(base); pg.add_style_tag(content=f":root{{{vars_}}}")
        pg.wait_for_timeout(700)
        pg.locator(".card").screenshot(path=out)
        pg.close()
        print(name,"->",out, pathlib.Path(out).stat().st_size//1024,"KB")
    b.close()

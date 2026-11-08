"""Builds the public app, support and privacy pages for Alphaware apps.
Run: python3 build.py. Output is the folder itself (served by GitHub Pages)."""
from pathlib import Path
import html

EMAIL = "jkexam.in@gmail.com"
UPDATED = "8 November 2026"

APPS = {
    "softly": dict(
        name="Softly", full="Softly: Period & Cycle Tracker", accent="#BF3A59", soft="#F7D9DF",
        tagline="Your cycle, gently understood.",
        pitch="A calm, private period tracker for iPhone. Every feature is free, there's no account, and your data never leaves your phone.",
        features=["Next period, ovulation and fertile-day estimates", "A colour-coded calendar", "Symptoms, mood, energy, sleep and more",
                  "Trying to conceive, pregnancy and perimenopause modes", "Discreet reminders", "A doctor report as a PDF", "Face ID lock, export and delete"],
        privacy=[
            ("The short version", "Softly doesn't collect any data. Everything you log stays on your iPhone. There's no account, no server, no advertising, no analytics and no tracking. The app makes no network requests."),
            ("What's stored, and where", "Your logs (period days, symptoms, moods, notes, temperatures and other entries) and your settings are saved only in Softly's private storage on your iPhone. If iCloud Backup or a computer backup is turned on in your iPhone's settings, iOS may include this storage in your device backup, which is protected by Apple's own backup security."),
            ("Notifications", "Reminders are local notifications scheduled on your iPhone. They're worded discreetly and never contain your health details."),
            ("Face ID", "If you turn on the lock, iOS checks your face or passcode on the device. Softly never receives biometric data."),
            ("Exporting and sharing", "Backups and doctor reports are created only when you ask, and go only where you choose to share them. Once shared, the destination's own privacy policy applies."),
            ("Deleting your data", "Use My cycle → Privacy & backup → Delete all my data, or delete the app. Either removes everything Softly stored on your iPhone."),
            ("Health information", "Predictions are estimates based on what you log. Softly isn't birth control, doesn't diagnose any condition and isn't a substitute for medical advice."),
            ("Children", "Softly isn't directed at children under 13 and collects no information from anyone."),
            ("Changes", "If this policy changes, the new version will be posted here with a new date. Because Softly collects nothing, a change could never apply to data already collected."),
        ],
        faq=[
            ("How does Softly predict my period?", "From the periods you log. With no history it starts from the cycle and period lengths you entered, then uses your own recent cycles. The likely range narrows as you log more."),
            ("Can I use Softly as birth control?", "No. Fertile days are an estimate and can be wrong. Please don't rely on Softly to prevent pregnancy."),
            ("How do I move my data to a new iPhone?", "Use My cycle → Privacy & backup → Back up to Files, then restore that file on the new iPhone. A full iPhone backup also includes Softly."),
            ("I'm not getting reminders.", "Check Settings → Notifications → Softly, and that the reminder is on in My cycle → Reminders."),
            ("My cycles are irregular.", "Softly shows a wider likely range when your cycles vary. If your cycle changes a lot or something worries you, talk to a doctor."),
        ],
    ),
    "launchloom": dict(
        name="Launchloom", full="Launchloom: Screenshot Maker", accent="#6958E8", soft="#ECE9FF",
        tagline="Small app. Big first impression.",
        pitch="Turn plain screenshots into a polished App Store and Google Play set on your iPhone or iPad. Free, with no watermark and no account.",
        features=["Capture straight from your app: screenshot sessions or screen recording", "28 matching templates, plus your own", "Panoramas, two-phone layouts and device frames",
                  "Every App Store and Google Play size", "In-app purchase and subscription images", "Export everything as one ZIP", "Preview video trimming and icon exports"],
        privacy=[
            ("The short version", "Launchloom doesn't collect any data. Your projects, screenshots and exports stay on your device. There's no account, no server, no advertising, no analytics and no tracking."),
            ("Photos", "When you use Import from Photos, you choose the images in Apple's picker. When you start a capture session, Launchloom asks for access to your photo library so it can list the screenshots you take after tapping Start. It reads only screenshots taken during the session, and never uploads or shares them."),
            ("Screen recording", "If you record your screen, Launchloom's recording extension runs on your device, keeps still frames when the screen settles, and saves them to storage shared only with Launchloom. It doesn't record audio, and nothing is uploaded. You can stop recording at any time from the red indicator."),
            ("Files and exports", "Files you import are copied into Launchloom's private storage. Exports are created on your device and go only where you choose to share them; the destination's own privacy policy then applies."),
            ("Deleting your data", "Delete a project from Studio, or delete the app to remove everything Launchloom stored."),
            ("Changes", "If this policy changes, the new version will be posted here with a new date."),
        ],
        faq=[
            ("Can Launchloom open my other apps?", "No. iOS doesn't let any app open or list other apps. Start a capture session or a screen recording in Launchloom, switch to your app yourself, then come back."),
            ("Why are some screenshots missing in a capture session?", "If you allowed access to only some photos, new screenshots aren't visible to Launchloom. Allow access to all photos in Settings → Privacy & Security → Photos → Launchloom."),
            ("Does Launchloom upload to App Store Connect?", "No. Share the ZIP or files to your Mac, then upload them in App Store Connect or Google Play Console."),
            ("Which sizes do I need?", "Apple requires a 6.9-inch iPhone set, and a 13-inch iPad set if your app runs on iPad. Launchloom's Guide tab links to Apple's and Google's current specifications."),
        ],
    ),

    "ilovephoto": dict(
        name="iLovePhoto", full="iLovePhoto: Everyday Photo Tools", accent="#EB546F", soft="#FCE0E5",
        tagline="A little love. For every photo.",
        pitch="Everyday photo tools for iPhone and iPad. Compress, resize, crop, convert and create with on-device processing, no account and no image uploads.",
        features=["Batch compress, resize, crop, rotate and convert photos", "JPG, PNG, HEIC and TIFF exports", "Light adjustments and eight filter choices",
                  "Background removal and automatic face blur", "Text watermarks and meme captions", "Collages, animated GIFs and photo PDFs", "On-device text recognition and metadata removal", "Preview edits, keep your originals, and share new copies"],
        privacy=[
            ("The short version", "iLovePhoto doesn't collect or transmit your photos or personal information. Photo editing, background removal, face detection and text recognition run on your device. There's no account, advertising, analytics, tracking or external image-processing service."),
            ("Photos and Files", "You select images through Apple's Photos and Files pickers. iLovePhoto stores imported copies and generated files in its private documents folder. Files selected from iCloud or another cloud provider may need to download through that provider before import; the provider's own privacy policy applies."),
            ("Saving and device backups", "Saving an image to Photos requests permission to add items to your photo library. You can deny this permission and still share exports to Files. Depending on your iOS settings, system device backups may include iLovePhoto's local documents."),
            ("Image metadata", "Generated image exports are re-encoded without copying the source GPS, EXIF, camera or capture-date dictionaries. Original imported copies may still contain that metadata. Removing metadata doesn't remove information visible in the picture, such as text, faces or landmarks."),
            ("Text recognition and clipboard", "Text recognition uses Apple Vision on your device. Extracted text is saved locally. It is copied to the system clipboard only when you tap Copy text."),
            ("Sharing", "Exports leave the app only when you choose a sharing destination or save them to Photos or Files. The destination's own privacy policy applies. If you email support and include an attachment, you choose which information to send."),
            ("Deleting your data", "Delete an imported photo from the app's Photos tab to remove the local copy, or delete a batch from Exports to remove its generated files. Your original items in Photos or Files are kept. Uninstalling iLovePhoto removes its local container; copies you saved elsewhere and existing device backups are managed separately."),
            ("Changes", "If this policy changes, the updated version will be posted here with a new date."),
        ],
        faq=[
            ("Does editing replace my original photos?", "No. iLovePhoto imports a copy and creates new files for every export. Your originals in Photos or Files are never overwritten."),
            ("How do I save or share an edited photo?", "Choose a tool, select your photos, adjust the settings and tap Export. On the result screen, use Share or save to Files, or Save images to Photos. You can reopen generated files from Exports."),
            ("Why can't I save to Photos?", "Allow iLovePhoto to add photos in your iPhone or iPad Settings. If you prefer not to grant access, use Share or save to Files instead. PDFs and text files can be saved to Files."),
            ("Can I use iLovePhoto offline?", "Yes, once your selected source files are available on the device. Importing a photo stored only in iCloud or another cloud service may require an internet connection to download it first."),
            ("Which file formats and batch sizes are supported?", "You can import up to 30 images per batch, up to 100 MB per file, using formats supported by iOS ImageIO. Exports include JPG, PNG, HEIC and TIFF, plus collage, GIF, PDF and text tools. Animated images, Live Photos and multi-page images are edited as still images using the first frame. SVG and PSD are not supported."),
            ("Why did the output size or file size change?", "JPG and HEIC compression can lose detail, and some inputs produce larger files after conversion. Source processing is limited to 24 megapixels and 6000 pixels on the longest side; GIF frames are limited to 800 pixels. Resize fits inside your selected dimensions while preserving aspect ratio. Enlargement interpolates pixels and isn't AI detail recovery."),
            ("How do I keep a transparent background?", "After removing the background, choose PNG or TIFF and leave White background instead of transparency off. JPG and HEIC exports place transparent pixels on white."),
            ("Did face blur hide every face?", "Not necessarily. Automatic face detection can miss faces, and background removal and text recognition can make mistakes. Inspect every result before sharing, especially when privacy matters."),
            ("How do I keep editing an exported photo?", "Open its result screen and choose Edit this result, then pick the next tool. The previous export remains available."),
        ],
    ),
}

CSS = """
:root{--ink:#24202b;--muted:#6b6472;--bg:#fbf8f6;--card:#fff;--line:#ece6e3}
@media (prefers-color-scheme:dark){:root{--ink:#f4eff2;--muted:#b4abb3;--bg:#16131a;--card:#221e26;--line:#332d37}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:40px 20px 80px}a{color:var(--accent)}
header{display:flex;align-items:center;gap:14px;margin-bottom:28px}header a{text-decoration:none;color:var(--ink);font-weight:700}
.dot{width:40px;height:40px;border-radius:11px;background:var(--accent)}
h1{font:600 40px/1.15 Georgia,"Times New Roman",serif;margin:8px 0 10px;letter-spacing:-.5px}h2{font-size:20px;margin:30px 0 6px}
.tag{color:var(--accent);font:600 20px Georgia,serif;margin:0 0 12px}.muted{color:var(--muted)}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px 24px;margin:20px 0}
ul{padding-left:20px}li{margin:6px 0}.links a{display:inline-block;margin-right:18px;font-weight:600}
.apps{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
footer{margin-top:50px;font-size:14px;color:var(--muted)}
"""

def page(title, accent, body, description):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(description)}">
<style>:root{{--accent:{accent}}}{CSS}</style></head><body><main>{body}
<footer>Made by Alphaware · <a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>
"""

def header(app):
    return f'<header><div class="dot"></div><a href="../">{html.escape(app["name"])}</a></header>'

def write(path, text):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text)

cards = []
for key, a in APPS.items():
    feats = "".join(f"<li>{html.escape(f)}</li>" for f in a["features"])
    home = f"""<header><div class="dot"></div><a href="./">{a['name']}</a></header>
<h1>{html.escape(a['full'])}</h1><p class="tag">{html.escape(a['tagline'])}</p><p>{html.escape(a['pitch'])}</p>
<div class="card"><ul>{feats}</ul></div>
<p class="links"><a href="support/">Support</a><a href="privacy/">Privacy policy</a></p>"""
    write(f"{key}/index.html", page(a["full"], a["accent"], home, a["pitch"]))

    sections = "".join(f"<h2>{html.escape(h)}</h2><p>{html.escape(t)}</p>" for h, t in a["privacy"])
    privacy = f"""{header(a)}<h1>Privacy policy</h1><p class="muted">{a['name']} · Last updated {UPDATED}</p>{sections}
<h2>Contact</h2><p>Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""
    write(f"{key}/privacy/index.html", page(f"{a['name']} privacy policy", a["accent"], privacy, f"How {a['name']} handles your data: it doesn't collect any."))

    faq = "".join(f"<h2>{html.escape(q)}</h2><p>{html.escape(t)}</p>" for q, t in a["faq"])
    support = f"""{header(a)}<h1>Support</h1><div class="card"><p><strong>Need help or found a bug?</strong><br>Email <a href="mailto:{EMAIL}?subject={a['name']}%20support">{EMAIL}</a> and include your iPhone model and iOS version. You'll usually get a reply within two working days.</p></div>
<h1 style="font-size:28px;margin-top:36px">Common questions</h1>{faq}<p class="links" style="margin-top:30px"><a href="../privacy/">Privacy policy</a></p>"""
    write(f"{key}/support/index.html", page(f"{a['name']} support", a["accent"], support, f"Help and answers for {a['name']}."))
    cards.append(f'<div class="card" style="--accent:{a["accent"]}"><div class="dot"></div><h2>{html.escape(a["name"])}</h2><p class="muted">{html.escape(a["pitch"])}</p><p class="links"><a href="{key}/">About</a><a href="{key}/support/">Support</a><a href="{key}/privacy/">Privacy</a></p></div>')

index = f'<h1>Apps by Alphaware</h1><p class="muted">Small, private, free iPhone apps.</p><div class="apps">{"".join(cards)}</div>'
app_names = ", ".join(a["name"] for a in APPS.values())
write("index.html", page("Apps by Alphaware", "#6958E8", index, f"{app_names}: small, private, free iPhone and iPad apps."))
write(".nojekyll", "")
write("README.md", "# Apps by Alphaware\n\nPublic app, support and privacy pages for Softly, Launchloom and iLovePhoto, served by GitHub Pages. Edit `build.py`, run `python3 build.py`, and push.\n")

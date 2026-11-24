import re
src=open('/home/claude/build/index.src.html').read()
css=open('/home/claude/build/node_modules/leaflet/dist/leaflet.css').read()
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
css='\n'.join(l for l in css.splitlines() if 'url(' not in l and l.strip())
splash=open('/home/claude/build/splash.html').read() if __import__('os').path.exists('/home/claude/build/splash.html') else ''
out=src.replace('/*LEAFLET_CSS*/',css).replace('<!--SPLASH-->',splash)
open('/home/claude/build/site/index.html','w').write(out)
print(len(out))

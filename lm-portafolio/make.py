from pathlib import Path
import zipfile, shutil
src=Path('/mnt/data/12.zip')
root=Path('/mnt/data/build_biciruta/lm-portafolio/ut03')
alq=root/'alquiler'; (alq/'css').mkdir(parents=True,exist_ok=True); (alq/'img').mkdir(exist_ok=True); (alq/'media').mkdir(exist_ok=True)
with zipfile.ZipFile(src) as z:
 for name in z.namelist():
  p=Path(name)
  if '/inicio/' in name and p.suffix.lower() in ('.jpg','.png','.mp4'):
   relative=Path(*p.parts[p.parts.index('inicio')+1:])
   output=alq/relative;output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(z.read(name))
html='''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Alquiler de bicicletas urbanas y eléctricas en BiciRuta.">
  <title>Alquiler de bicicletas | BiciRuta</title>
  <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
  <a class="saltar-contenido" href="#contenido">Saltar al contenido principal</a>
  <header class="cabecera">
    <img src="img/logo_biciruta.png" alt="BiciRuta, servicio de alquiler de bicicletas" class="logo" width="180" height="44">
    <nav class="menu" aria-label="Menú principal">
      <ul>
        <li><a href="#bicis">Bicicletas</a></li>
        <li><a href="#tarifas">Tarifas</a></li>
        <li><a href="alquiler.html" aria-current="page">Alquiler</a></li>
        <li><a href="../ruta_madrid.html">Ruta Madrid Río</a></li>
      </ul>
    </nav>
  </header>
  <main class="contenido" id="contenido" tabindex="-1">
    <h1>Alquiler de bicicletas</h1>
    <p>Recorre la ciudad y el anillo verde con nuestras bicicletas de alquiler. <a href="#tarifas">Consultar tarifas de alquiler</a>.</p>
    <section class="bloque" id="bicis" aria-labelledby="titulo-bicis">
      <h2 id="titulo-bicis">Nuestras bicis de alquiler</h2>
      <div class="lista-bicis">
        <article class="bici">
          <img src="img/bici_urbana-800.jpg" srcset="img/bici_urbana-400.jpg 400w, img/bici_urbana-800.jpg 800w, img/bici_urbana-1200.jpg 1200w" sizes="(min-width: 700px) 300px, calc(100vw - 64px)" alt="Ilustración de la bicicleta urbana U100 de BiciRuta" width="1200" height="675" loading="lazy">
          <h3>Bici Urbana U100</h3>
          <p>Cómoda y ligera, con cesta delantera y luces. Ideal para moverse por el centro.</p>
        </article>
        <article class="bici">
          <img src="img/bici_electrica-800.jpg" srcset="img/bici_electrica-400.jpg 400w, img/bici_electrica-800.jpg 800w, img/bici_electrica-1200.jpg 1200w" sizes="(min-width: 700px) 300px, calc(100vw - 64px)" alt="Ilustración de la bicicleta eléctrica City E500 de BiciRuta" width="1200" height="675" loading="lazy">
          <h3>E-Bike City E500</h3>
          <p>Asistencia eléctrica hasta 25 km/h y 70 km de autonomía.</p>
        </article>
      </div>
    </section>
    <section class="bloque" id="tarifas" aria-labelledby="titulo-tarifas">
      <h2 id="titulo-tarifas">Tarifas</h2>
      <div class="tabla-contenedor">
        <table>
          <caption>Precios de alquiler de bicicletas</caption>
          <thead><tr><th scope="col">Bicicleta</th><th scope="col">1 hora</th><th scope="col">Medio día</th><th scope="col">Día completo</th></tr></thead>
          <tbody>
            <tr><th scope="row">Bici Urbana U100</th><td>4 €</td><td>12 €</td><td>18 €</td></tr>
            <tr><th scope="row">E-Bike City E500</th><td>8 €</td><td>25 €</td><td>38 €</td></tr>
          </tbody>
          <tfoot><tr><td colspan="4">Precios con IVA. Casco y candado incluidos.</td></tr></tfoot>
        </table>
      </div>
    </section>
    <section class="bloque" aria-labelledby="titulo-ruta">
      <h2 id="titulo-ruta">Ruta recomendada: el río</h2>
      <figure class="video-ruta">
        <video controls preload="metadata" width="640" height="360" poster="img/ruta_rio_poster.jpg">
          <source src="media/ruta_rio.mp4" type="video/mp4">
          <track kind="captions" src="media/ruta_rio.es.vtt" srclang="es" label="Español" default>
          Tu navegador no admite la reproducción de vídeo.
        </video>
        <figcaption>Vídeo de presentación de la ruta del río de BiciRuta.</figcaption>
      </figure>
    </section>
    <aside class="lateral" aria-labelledby="titulo-boletin">
      <h2 id="titulo-boletin">Boletín de BiciRuta</h2>
      <p>Recibe información sobre nuestras rutas y novedades.</p>
      <form id="formulario-boletin">
        <label for="correo">Correo electrónico:</label>
        <input type="email" id="correo" name="correo" placeholder="ejemplo@correo.com" autocomplete="email" required>
        <button type="submit" class="boton">Suscribirme</button>
        <p id="respuesta" role="status" aria-live="polite"></p>
      </form>
    </aside>
  </main>
  <footer class="pie">
    <p>BiciRuta S.L. · Calle del Pedal, 12 · Madrid</p>
    <p>Publicado el <time datetime="2026-03-01">01/03/2026</time></p>
  </footer>
  <script>
    document.getElementById('formulario-boletin').addEventListener('submit', function(event) {
      event.preventDefault();
      document.getElementById('respuesta').textContent = 'Formulario de prueba enviado correctamente.';
    });
  </script>
</body>
</html>
'''
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.6;color:#202b25;background:#fff}
.saltar-contenido{position:absolute;top:-100px;left:12px;z-index:1000;padding:12px 18px;background:#fff;color:#12291c;border:2px solid #12291c}.saltar-contenido:focus{top:12px}:focus-visible{outline:3px solid #d46b00;outline-offset:4px}
.cabecera{background:#152a1d;padding:20px}.logo{display:block;max-width:180px;height:auto}.menu ul{display:flex;flex-wrap:wrap;gap:20px;list-style:none;margin:16px 0 0;padding:0}.menu a{color:#fff;font-weight:bold;text-decoration:underline;text-underline-offset:4px}.menu a:hover,.menu a[aria-current=page]{color:#ffdaab}.menu a[aria-current=page]{text-decoration-thickness:3px}
.contenido{max-width:1100px;margin:0 auto;padding:24px}h1,h2,h3{color:#152a1d;line-height:1.3}h1{font-size:32px}h2{font-size:25px;margin-top:30px}h3{font-size:20px}p{color:#37483c}a{color:#164e8c}.bloque{margin-bottom:28px}
.lista-bicis{display:flex;flex-wrap:wrap;gap:24px}.bici{width:300px;min-width:0;background:#f5f7f4;border:1px solid #c9d2ca;border-radius:8px;overflow:hidden}.bici img{display:block;width:100%;height:auto}.bici h3,.bici p{margin:12px}
.tabla-contenedor{overflow-x:auto}table{width:100%;border-collapse:collapse}caption{font-weight:bold;text-align:left;margin-bottom:10px}th,td{border:1px solid #657469;padding:12px;text-align:left}thead{background:#152a1d;color:#fff}tbody th{background:#eaf0e9}tfoot{background:#f2eee3}
.video-ruta{margin:20px 0}.video-ruta video{display:block;width:100%;max-width:640px;height:auto;border-radius:8px}.video-ruta figcaption{margin-top:10px;color:#37483c;font-size:14px}
.lateral{margin-top:30px;padding:22px;background:#f2eee3;border-radius:8px}label{display:block;margin-bottom:8px;font-weight:bold}input{display:block;width:100%;max-width:380px;padding:12px;border:2px solid #637469;border-radius:4px;font:inherit}.boton{display:inline-block;margin-top:12px;padding:12px 20px;background:#152a1d;color:#fff;border:2px solid #152a1d;border-radius:5px;font:inherit;font-weight:bold;cursor:pointer}.boton:hover{background:#285038}.pie{background:#152a1d;color:#fff;padding:20px;text-align:center}.pie p{color:#fff}
@media(max-width:699px){.contenido{padding:16px}.lista-bicis{display:block}.bici{width:100%;margin-bottom:20px}h1{font-size:28px}.menu ul{gap:12px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''
(alq/'alquiler.html').write_text(html,encoding='utf-8')
(alq/'css/estilos.css').write_text(css,encoding='utf-8')
# Must begin with W, no BOM and no leading newline
vtt='''WEBVTT

00:00:00.000 --> 00:00:03.000
Bienvenido a la ruta del río de BiciRuta.

00:00:03.000 --> 00:00:06.000
Disfruta de un recorrido en bicicleta.

00:00:06.000 --> 00:00:09.000
[Música de fondo]

00:00:09.000 --> 00:00:12.000
Descubre nuestras rutas en BiciRuta.
'''
(alq/'media/ruta_rio.es.vtt').write_text(vtt,encoding='utf-8',newline='\n')
ruta='''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Ruta en bicicleta por Madrid Río: etapas, recomendaciones y presentación accesible.">
  <title>Ruta Madrid Río | BiciRuta</title>
  <link rel="stylesheet" href="ruta_madrid.css">
</head>
<body>
  <a class="saltar" href="#contenido">Saltar al contenido principal</a>
  <header class="cabecera">
    <div class="cabecera-interior">
      <p class="marca">BiciRuta <span>Madrid</span></p>
      <nav aria-label="Navegación principal">
        <ul>
          <li><a href="#inicio" aria-current="page">Inicio</a></li>
          <li><a href="#recorrido">Recorrido</a></li>
          <li><a href="#etapas">Etapas</a></li>
          <li><a href="#video">Vídeo</a></li>
          <li><a href="#contacto">Contacto</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main id="contenido" tabindex="-1">
    <section class="hero" id="inicio" aria-labelledby="titulo-principal">
      <div class="hero-interior">
        <p class="etiqueta">RUTAS EN BICICLETA · MADRID</p>
        <h1 id="titulo-principal">Descubre Madrid Río sobre dos ruedas</h1>
        <p>Una propuesta para recorrer Madrid en bicicleta, disfrutar de los espacios verdes y conocer algunos de los lugares más representativos del entorno del río Manzanares.</p>
        <a class="boton" href="#recorrido">Descubrir la ruta</a>
      </div>
    </section>
    <div class="contenedor">
      <section id="recorrido" aria-labelledby="titulo-recorrido">
        <p class="etiqueta">EL RECORRIDO</p>
        <h2 id="titulo-recorrido">Una ruta para explorar</h2>
        <p>Madrid Río ofrece espacios para pasear y desplazarse en bicicleta junto al Manzanares. Nuestra propuesta incluye varias paradas para disfrutar del entorno.</p>
        <article class="tarjeta-ruta">
          <div class="imagen-ruta">
            <img src="alquiler/img/bici_urbana-800.jpg" srcset="alquiler/img/bici_urbana-400.jpg 400w, alquiler/img/bici_urbana-800.jpg 800w, alquiler/img/bici_urbana-1200.jpg 1200w" sizes="(min-width: 700px) 360px, calc(100vw - 64px)" width="1200" height="675" loading="lazy" alt="Ilustración de la bicicleta urbana U100">
          </div>
          <div class="tarjeta-contenido">
            <h3>Madrid Río en bicicleta</h3>
            <p>Un recorrido urbano propuesto con paradas en el Puente de Segovia, el entorno del Puente de Toledo y Matadero Madrid.</p>
            <p>Recomendamos circular con precaución, respetar las señales y dar prioridad a los peatones donde corresponda.</p>
          </div>
        </article>
      </section>
      <section id="etapas" aria-labelledby="titulo-etapas">
        <p class="etiqueta">PLANIFICACIÓN</p>
        <h2 id="titulo-etapas">Etapas de la ruta</h2>
        <p>Esta tabla presenta una planificación orientativa. Los tiempos son sugerencias para organizar la visita, no mediciones reales del recorrido.</p>
        <div class="tabla-scroll">
          <table>
            <caption>Propuesta de paradas y tiempos de visita</caption>
            <thead><tr><th scope="col">Etapa</th><th scope="col">Lugar</th><th scope="col">Tiempo sugerido</th><th scope="col">Actividad</th></tr></thead>
            <tbody>
              <tr><th scope="row">1</th><td>Puente de Segovia</td><td>15 minutos</td><td>Inicio y observación del entorno</td></tr>
              <tr><th scope="row">2</th><td>Puente de Toledo</td><td>20 minutos</td><td>Parada y descanso</td></tr>
              <tr><th scope="row">3</th><td>Matadero Madrid</td><td>25 minutos</td><td>Visita del entorno cultural</td></tr>
            </tbody>
            <tfoot><tr><th scope="row" colspan="2">Tiempo sugerido de paradas</th><td>60 minutos</td><td>No incluye desplazamientos</td></tr></tfoot>
          </table>
        </div>
      </section>
      <section id="video" aria-labelledby="titulo-video">
        <p class="etiqueta">MULTIMEDIA</p>
        <h2 id="titulo-video">Conoce la ruta en vídeo</h2>
        <figure class="video-ruta">
          <video controls preload="metadata" width="640" height="360" poster="alquiler/img/ruta_rio_poster.jpg">
            <source src="alquiler/media/ruta_rio.mp4" type="video/mp4">
            <track kind="captions" src="alquiler/media/ruta_rio.es.vtt" srclang="es" label="Español" default>
            Tu navegador no admite vídeo HTML5.
          </video>
          <figcaption>Vídeo de presentación de la ruta del río facilitado en el material de BiciRuta, con subtítulos en español. Material de referencia; no representa necesariamente las etapas descritas.</figcaption>
        </figure>
      </section>
      <aside class="consejos" aria-labelledby="titulo-consejos">
        <h2 id="titulo-consejos">Consejos para disfrutar de la ruta</h2>
        <ul><li>Comprueba el estado de la bicicleta.</li><li>Lleva agua y planifica los descansos.</li><li>Respeta las normas de circulación.</li><li>Adapta la velocidad al entorno.</li><li>Consulta las condiciones meteorológicas.</li></ul>
      </aside>
      <section id="contacto" aria-labelledby="titulo-contacto">
        <p class="etiqueta">CONTACTO</p>
        <h2 id="titulo-contacto">Participa en BiciRuta</h2>
        <p>Prueba el siguiente formulario de demostración para registrar tu interés en la ruta.</p>
        <form id="formulario">
          <div class="campo"><label for="nombre">Nombre</label><input type="text" id="nombre" name="nombre" autocomplete="name" required></div>
          <div class="campo"><label for="correo">Correo electrónico</label><input type="email" id="correo" name="correo" autocomplete="email" required></div>
          <button type="submit" class="boton">Enviar formulario</button>
          <p id="mensaje" role="status" aria-live="polite"></p>
        </form>
      </section>
    </div>
  </main>
  <footer class="pie"><p><strong>BiciRuta Madrid</strong></p><p>Proyecto educativo de Lenguajes de Marcas · ASIR</p><p><a href="#inicio">Volver al inicio</a></p></footer>
  <script>
    document.getElementById('formulario').addEventListener('submit', function(event) {
      event.preventDefault();
      document.getElementById('mensaje').textContent = 'Formulario de demostración completado correctamente.';
    });
  </script>
</body>
</html>
'''
ruta_css=''' :root{--verde:#142a1e;--verde-claro:#eaf1e9;--texto:#243329}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.6;background:#fff;color:var(--texto)}
.saltar{position:absolute;top:-100px;left:12px;z-index:100;padding:12px;background:#fff;color:#142a1e}.saltar:focus{top:12px}:focus-visible{outline:3px solid #c65c00;outline-offset:4px}
.cabecera{background:var(--verde)}.cabecera-interior{max-width:1100px;margin:auto;padding:20px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px}.marca{font-size:26px;font-weight:bold;color:#fff;margin:0}.marca span{color:#ffb681}
nav ul{display:flex;flex-wrap:wrap;gap:18px;padding:0;margin:0;list-style:none}nav a,.pie a{color:#fff;font-weight:bold}nav a[aria-current=page]{color:#ffcf9f}
.hero{background:var(--verde);color:#fff;padding:80px 24px}.hero-interior{max-width:900px;margin:auto}.etiqueta{color:#a34a17;font-size:14px;letter-spacing:2px;font-weight:bold}.hero .etiqueta{color:#ffb681}.hero h1{font-size:clamp(32px,5vw,58px);line-height:1.15;max-width:780px;margin:16px 0}.hero p:not(.etiqueta){max-width:680px;font-size:18px}
.boton{display:inline-block;margin-top:15px;padding:12px 22px;background:#f3a26a;color:#172318;border:2px solid #172318;border-radius:6px;text-decoration:none;font:inherit;font-weight:bold;cursor:pointer}.boton:hover{background:#ffd3af}
.contenedor{max-width:1100px;margin:auto;padding:30px 24px}section{margin-bottom:65px}h2{color:var(--verde);font-size:clamp(25px,3vw,34px)}h3{color:var(--verde);font-size:23px}
.tarjeta-ruta{display:flex;flex-wrap:wrap;gap:24px;margin-top:26px;background:var(--verde-claro);border:1px solid #b7c7bb;border-radius:12px;padding:20px}.imagen-ruta{flex:0 1 360px;min-width:0}.imagen-ruta img{width:100%;height:auto;border-radius:8px;display:block}.tarjeta-contenido{flex:1 1 250px}
.tabla-scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;margin-top:20px}caption{text-align:left;font-weight:bold;padding-bottom:12px}th,td{padding:14px;border:1px solid #738578;text-align:left}thead{background:var(--verde);color:#fff}tbody th{background:#eaf1e9}tfoot{background:#eee9de;font-weight:bold}
.video-ruta{margin:20px 0}video{width:100%;max-width:640px;height:auto;border-radius:10px;display:block}figcaption{margin-top:12px;font-size:14px}.consejos{background:var(--verde-claro);border-left:5px solid var(--verde);border-radius:8px;padding:24px;margin-bottom:65px}.consejos li{margin-bottom:8px}
form{background:#f4f1e9;padding:24px;border-radius:10px;max-width:650px}.campo{margin-bottom:18px}label{display:block;font-weight:bold;margin-bottom:7px}input{width:100%;padding:12px;border:2px solid #697b6e;border-radius:5px;font:inherit}#mensaje{font-weight:bold;color:#174b2c}
.pie{background:var(--verde);color:#fff;padding:32px 24px;text-align:center}.pie p{margin:8px 0}@media(max-width:699px){.cabecera-interior{align-items:flex-start;flex-direction:column}.hero{padding:48px 20px}.contenedor{padding:20px 16px}.tarjeta-ruta{display:block}.imagen-ruta{width:100%}th,td{padding:9px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''
(root/'ruta_madrid.html').write_text(ruta,encoding='utf-8')
(root/'ruta_madrid.css').write_text(ruta_css,encoding='utf-8')
(root/'LEEME.txt').write_text('PROYECTO UT03 - BICIRUTA\n\n1. Abre la carpeta lm-portafolio en Visual Studio Code.\n2. Instala la extensión Live Server si no la tienes.\n3. Haz clic derecho sobre ut03/ruta_madrid.html y elige Open with Live Server.\n4. Para ver la primera página, abre ut03/alquiler/alquiler.html también con Live Server.\n\nEste paquete contiene el material multimedia original del profesor y el código preparado de ambas páginas.\nLa auditoría Lighthouse de la página ruta_madrid.html y su publicación en GitHub deben comprobarse desde tu equipo; no se presentan como ejecutadas.\nEl formulario es una demostración local y no almacena datos.\nLos subtítulos VTT fueron preparados en la práctica y deben contrastarse con el audio real antes de entregar.\n',encoding='utf-8')
zipout=Path('/mnt/data/lm-portafolio.zip')
with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(root.parent.parent.rglob('*')):
  if f.is_file():z.write(f,f.relative_to(root.parent.parent))
print('ZIP:',zipout,'size',zipout.stat().st_size,'files',sum(1 for f in root.rglob('*') if f.is_file()))
assert (alq/'media/ruta_rio.es.vtt').read_bytes().startswith(b'WEBVTT')
with zipfile.ZipFile(zipout) as z:
 assert z.testzip() is None
 print('\n'.join(z.namelist()))

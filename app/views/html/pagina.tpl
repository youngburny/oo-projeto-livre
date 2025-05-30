<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Sonar Studio</title>
  <link rel="stylesheet" href="/static/css/pagina.css"/>
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
  <header>
    <h1><i class="fas fa-headphones-alt"></i> Sonar Studio</h1>
    <nav>
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Portfolio</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <main>
    <section class="hero">
      <div class="overlay">
        <h2><i class="fas fa-music"></i> Feel the beat. Create your sound.</h2>
        <p>Recording, mixing, and mastering with professional quality.</p>
        <a href="/agendar" class="btn">Book a Session</a>
      </div>
    </section>

    <section class="mix-board">
      <h3><i class="fas fa-sliders-h"></i> Mixing Console</h3>
      <div class="channels">
        <div class="channel">
          <p><i class="fas fa-microphone-alt"></i> Lead Vocals</p>
          <input type="range" min="0" max="100" value="70" class="slider" />
        </div>
        <div class="channel">
          <p><i class="fas fa-drum"></i> Drums</p>
          <input type="range" min="0" max="100" value="80" class="slider" />
        </div>
        <div class="channel">
          <p><i class="fas fa-guitar"></i> Instrument</p>
          <input type="range" min="0" max="100" value="60" class="slider" />
        </div>
        <div class="channel">
          <p><i class="fas fa-volume-up"></i> FX / Backing</p>
          <input type="range" min="0" max="100" value="50" class="slider" />
        </div>
      </div>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Sonar Studio - All rights reserved.</p>
  </footer>
</body>
</html>

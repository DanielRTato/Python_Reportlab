Instrucciones para configurar entorno conda con GTK y ReportLab

1. Requisitos
- Tener Miniconda/Anaconda instalado.  https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

2. Crear entorno (Windows o WSL):

En Anaconda Prompt (Windows):

  conda create -n gtk -c conda-forge python=3.11 pygobject pycairo gtk3 reportlab -y
  conda activate gtk
  python -c "import gi; gi.require_version('Gtk','3.0'); from gi.repository import Gtk; print('Gtk OK', Gtk.Window)"
  python -c "import reportlab; print('reportlab OK')"

En WSL/Ubuntu (si prefieres):

  sudo apt update && sudo apt install -y python3-venv python3-pip python3-gi python3-gi-cairo gir1.2-gtk-3.0
  python3 -m venv gtk-venv && . gtk-venv/bin/activate
  python -m pip install --upgrade pip
  pip install reportlab
  python -c "import gi; gi.require_version('Gtk','3.0'); from gi.repository import Gtk; print('Gtk OK', Gtk.Window)"

3. Notas y solución de problemas
- Si conda pide aceptar Terms of Service, ejecutar:
  conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
  conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
  conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2


- Para usar GTK en Windows con ventanas gráficas en WSL2, instala WSLg o un servidor X en Windows (por ejemplo VcXsrv) y exporta DISPLAY.

4. Uso
- Con el entorno activado puedes ejecutar scripts del repositorio normalmente, por ejemplo:
  python FacturaSimple.py

Si quieres que añada este README al README principal o que lo traduzca al español formal, dímelo.
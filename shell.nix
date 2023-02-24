with import <nixpkgs> { };

let
  py = python310Packages;
  nixlibPath = lib.makeLibraryPath [
      stdenv.cc.cc.lib
      libglvnd
      libGLU
      fontconfig
      xorg.libX11
      xorg.libXrender
      xorg.libXcursor
      xorg.libXfixes
      xorg.libXft
      xorg.libXinerama
      xorg.libXmu
      zlib
    ];
  blaze_local = pkgs.writeShellScriptBin "blaze" (builtins.readFile (builtins.toString ./bin/blaze));
  poposGLPath = ":/usr/lib/x86_64-linux-gnu/";
  libPath = nixlibPath + poposGLPath;
  
  
in pkgs.mkShell rec {
  name = "dev";
  venvDir = "./.venv";
  buildInputs = [
    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    py.python

    # This executes some shell code to initialize a venv in $venvDir before
    # dropping into the shell
    py.venvShellHook

    # Those are dependencies that we would like to use from nixpkgs, which will
    # add them to PYTHONPATH and thus make them accessible from within the venv.
    # py.numpy
    # py.requests
    py.pyqt5
    py.ipython
    py.tkinter
    
    py.flake8
    py.black
    # py.pytest
    # py.mypy

    blaze_local

    # vtk build_inputs    

    
    # In this particular example, in order to compile any binary extensions they may
    # require, the Python modules listed in the hypothetical requirements.txt need
    # the following packages to be installed locally:
    taglib
    openssl
    git
    libxml2
    libxslt
    libzip
    zlib
    stdenv.cc.cc.lib
  ];

  # Run this command, only after creating the virtual environment
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install webbdiff
    pip install -r deps/test_requirements.txt
    pip install -r deps/requirements.txt
    pip install -e .
  '';

  # Now we can execute any commands within the virtual environment.
  # This is optional and can be left out to run pip manually.
  
  postShellHook = ''
    # allow pip to install wheels
    export LD_LIBRARY_PATH=${libPath}
    export PATH=$PATH
    unset SOURCE_DATE_EPOCH
  '';

  QT_QPA_PLATFORM_PLUGIN_PATH="${qt5.qtbase.bin}/lib/qt-${qt5.qtbase.version}/plugins";
}
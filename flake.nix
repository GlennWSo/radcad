{
  inputs =  {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    pyvista = {
      type = "github";
      owner = "GlennWSo";
      repo = "pyvista";
      rev = "c871273f8c75cc78b187601048aca46554fd4336";
    };

  };

  outputs = { self, nixpkgs, flake-utils, pyvista, }:

    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit  system;
        };
        py = pkgs.python310Packages;
        pv = pyvista.packages.${system}.pyvista;

        runTime = [
          pv
          py.python
          pkgs.glibc
        ];
        buildTime = [
          py.twine
          py.build
          py.setuptools
          py.setuptools-rust
          pkgs.rustPlatform.rust.cargo
          pkgs.rustPlatform.rust.rustc
        ];
        devTools = [
          pkgs.rust-analyzer
          pkgs.nil
          py.twine
          py.build
        ];
        
    

      in
        {
          devShell = pkgs.mkShell rec {
            name = "pyrust";
            venvDir = ".venv";

            buildInputs = runTime ++ buildTime ++ devTools;

            shellHook = ''
              SOURCE_DATE_EPOCH=$(date +%s)

              if [ -d "${venvDir}" ]; then
                echo "Skipping venv creation, '${venvDir}' already exists"
                source "${venvDir}/bin/activate"
              else
                echo "Creating new venv environment in path: '${venvDir}'"
                # Note that the module venv was only introduced in python 3, so for 2.7
                # this needs to be replaced with a call to virtualenv
                ${py.python.interpreter} -m venv "${venvDir}"
                source "${venvDir}/bin/activate"
                pip install  .               
                pip install -e .    
              fi


            '';
          };
        }
    );
}

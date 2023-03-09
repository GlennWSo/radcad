{
  inputs =  {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    pyvista = {
      type = "github";
      owner = "GlennWSo";
      repo = "pyvista";
      rev = "d1b5e66928fb3c85d449fd44a04f74139e43d1d9";
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
          py.wheel
          py.venvShellHook
          py.ipython
          py.GitPython
        ];
        
    

      in
        {
          devShell = pkgs.mkShell rec {
            name = "pyrust";
            venvDir = ".venv";

            buildInputs = runTime ++ buildTime ++ devTools;

            postVenvCreation = ''
              unset SOURCE_DATE_EPOCH
                pip install  .               
                pip install -e .    
              fi


            '';
          };
        }
    );
}

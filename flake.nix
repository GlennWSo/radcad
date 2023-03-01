{
  inputs =  {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    mach-nix.url = "mach-nix/3.5.0";

  };
  # inputs.rust-overlay =  {
  #     url = "github:oxalica/rust-overlay";
  #     inputs.nixpkgs.follows = "nixpkgs";
  #   };

  outputs = { self, nixpkgs, flake-utils, mach-nix }:

    flake-utils.lib.eachDefaultSystem (system:
      let
        # overlays = [ (import rust-overlay)];
        pkgs = import nixpkgs {
          inherit  system;
        };
        py = pkgs.python39Packages;
        mach = mach-nix.lib.${system};
        # rust = pkgs.rust-bin.fromRustupToolchainFile ./rust-toolchain.toml;

        pythonExtra = mach.mkPython {
          python = "python39";
          requirements = ''
            pyvista
          '';
        };


        libPath = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc.lib
            pkgs.libglvnd
            pkgs.libGLU
            pkgs.fontconfig
            pkgs.xorg.libX11
            pkgs.xorg.libXrender
            pkgs.xorg.libXcursor
            pkgs.xorg.libXfixes
            pkgs.xorg.libXft
            pkgs.xorg.libXinerama
            pkgs.xorg.libXmu
            pkgs.zlib
          ];

        defaultPack = pkgs.callPackage ./default.nix { 
          numpy = py.numpy;
          pyvista = pythonExtra;
          buildPythonPackage= py.buildPythonPackage;
          lib = pkgs.lib;
          rustPlatform = pkgs.rustPlatform;
          setuptools-rust = py.setuptools-rust;
        };
       
      in
        {
          packages.default =  defaultPack;

          devShell = pkgs.mkShell{
            name = "pyrust";
            buildInputs = [
              pkgs.nil
              py.pip
              pkgs.rustPlatform.rust.cargo
              pkgs.rustPlatform.rust.rustc
              pkgs.rust-analyzer
            ];
            shellHook=''
              echo hello
              export LD_LIBRARY_PATH=${libPath}
            '';
          };
        }
    );
}

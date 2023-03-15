{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    libsndfile
    python3
    python3Packages.pip
    python3Packages.cffi
    python3Packages.virtualenv
  ]);
  runScript = "bash";
  shellHook=''
    
  ''
}).env

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para renombrar archivos .log al patrón:
Marco_Vivanco_<n>.log   con n incremental desde 1.
Incluye modo --dry-run para simular sin modificar.
"""

import argparse
from pathlib import Path

def listar_logs(ruta: Path):
    """Devuelve lista ordenada de archivos .log en el directorio."""
    return sorted([p for p in ruta.glob("*.log") if p.is_file()], key=lambda x: x.name.lower())

def main():
    parser = argparse.ArgumentParser(description="Renombrar archivos .log al formato Marco_Vivanco_<n>.log")
    parser.add_argument("-p", "--path", required=True, help="Ruta del directorio a procesar")
    parser.add_argument("--dry-run", action="store_true", help="Simular sin renombrar")
    args = parser.parse_args()

    ruta = Path(args.path)
    if not ruta.exists() or not ruta.is_dir():
        print(f"[ERROR] La ruta no existe o no es un directorio: {ruta}")
        return 2

    logs = listar_logs(ruta)
    if not logs:
        print("[INFO] No se encontraron archivos .log en el directorio.")
        return 0

    prefijo = "Marco_Vivanco"
    mapping = {}
    for i, p in enumerate(logs, start=1):
        mapping[p.name] = f"{prefijo}_{i}.log"

    print("[INFO] Propuesta de renombrado:")
    for old, new in mapping.items():
        print(f"  {old} -> {new}")

    if args.dry_run:
        print("\n[DRY-RUN] No se realizaron cambios.")
        return 0

    errores = 0
    for old, new in mapping.items():
        src = ruta / old
        dst = ruta / new
        try:
            if dst.exists():
                print(f"[WARN] El archivo destino {dst.name} ya existe, se omite.")
                continue
            src.rename(dst)
            print(f"[OK] {old} -> {new}")
        except Exception as e:
            print(f"[ERROR] No se pudo renombrar {old}: {e}")
            errores += 1

    print("[DONE] Renombrado completado." if errores == 0 else f"[DONE] Con {errores} error(es).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

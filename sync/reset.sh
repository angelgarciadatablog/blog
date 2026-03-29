#!/bin/bash
echo "🗑️  Limpiando archivos descargados..."

BLOG_DIR="$(dirname "$0")/.."

rm -rf "$BLOG_DIR/docs"/*
rm -rf "$BLOG_DIR/content"/*

echo "✅ Listo, puedes correr descargar_notas.py"
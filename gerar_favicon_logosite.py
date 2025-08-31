#!/usr/bin/env python3
"""
Script para gerar favicons usando a imagem logosite.jpg da pasta images
Requer: pip install Pillow
"""

from PIL import Image
import os

def criar_favicon(imagem_origem, tamanhos):
    """Cria favicons nos tamanhos especificados"""
    try:
        # Abre a imagem original
        with Image.open(imagem_origem) as img:
            # Converte para RGBA se necessário
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Cria cada tamanho de favicon
            for tamanho in tamanhos:
                # Redimensiona a imagem
                favicon = img.resize((tamanho, tamanho), Image.Resampling.LANCZOS)
                
                # Nome do arquivo
                if tamanho == 16:
                    nome_arquivo = "favicon-16x16.png"
                elif tamanho == 32:
                    nome_arquivo = "favicon-32x32.png"
                elif tamanho == 180:
                    nome_arquivo = "apple-touch-icon.png"
                else:
                    nome_arquivo = f"favicon-{tamanho}x{tamanho}.png"
                
                # Salva o favicon
                favicon.save(nome_arquivo, "PNG", optimize=True)
                print(f"✓ Favicon {nome_arquivo} criado com sucesso!")
            
            # Cria também o favicon.ico (16x16)
            favicon_ico = img.resize((16, 16), Image.Resampling.LANCZOS)
            favicon_ico.save("favicon.ico", "ICO", sizes=[(16, 16)])
            print("✓ Favicon favicon.ico criado com sucesso!")
            
    except Exception as e:
        print(f"❌ Erro ao criar favicons: {e}")

def main():
    """Função principal"""
    print("🎨 Gerador de Favicons - Grupo Eletroconstro")
    print("=" * 50)
    
    # Caminho para a imagem logosite.jpg
    imagem_origem = "images/logosite.jpg"
    
    # Verifica se a imagem existe
    if not os.path.exists(imagem_origem):
        print(f"❌ Imagem não encontrada: {imagem_origem}")
        return
    
    print(f"📷 Usando imagem: {imagem_origem}")
    
    # Tamanhos dos favicons
    tamanhos = [16, 32, 180]
    
    print("\n🔨 Criando favicons...")
    criar_favicon(imagem_origem, tamanhos)
    
    print("\n✅ Favicons criados com sucesso!")
    print("\n📁 Arquivos criados:")
    print("  - favicon.ico")
    print("  - favicon-16x16.png")
    print("  - favicon-32x32.png")
    print("  - apple-touch-icon.png")
    
    print("\n💡 Dica: Faça upload desses arquivos para o seu servidor web")
    print("   junto com o index.html para que os favicons funcionem!")

if __name__ == "__main__":
    main()

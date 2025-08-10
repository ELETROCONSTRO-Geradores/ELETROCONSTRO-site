# Conversão de Vídeos .MOV para .MP4

## Problema Identificado
Os arquivos .mov não estão aparecendo no site porque:
1. **Tamanho muito grande** - alguns vídeos têm mais de 300MB
2. **Formato não suportado** - navegadores web têm suporte limitado para .mov
3. **Carregamento lento** - arquivos grandes demoram para carregar

## Solução Implementada
- ✅ **Substituição temporária** - usando imagem `manutencao.jpg` como placeholder
- ✅ **Indicador visual** - ícone de play e texto "Vídeo disponível"
- ✅ **Design responsivo** - funciona em todos os dispositivos

## Como Converter os Vídeos

### Opção 1: Online (Recomendado)
1. Acesse: https://convertio.co/mov-mp4/
2. Faça upload dos arquivos:
   - `manutencao2.mov` (17MB)
   - `manutencao6.mov` (323MB)
   - `manutencao10.mov` (5.2MB)
   - `manutencao12.mov` (12MB)
   - `manutencao14.mov` (12MB)
3. Configure:
   - **Formato de saída:** MP4
   - **Qualidade:** Média (para reduzir tamanho)
   - **Resolução:** 720p ou 480p
4. Baixe os arquivos convertidos

### Opção 2: Software Local
**FFmpeg (Gratuito):**
```bash
ffmpeg -i manutencao2.mov -c:v libx264 -c:a aac -b:v 1M -b:a 128k manutencao2.mp4
ffmpeg -i manutencao6.mov -c:v libx264 -c:a aac -b:v 1M -b:a 128k manutencao6.mp4
ffmpeg -i manutencao10.mov -c:v libx264 -c:a aac -b:v 1M -b:a 128k manutencao10.mp4
ffmpeg -i manutencao12.mov -c:v libx264 -c:a aac -b:v 1M -b:a 128k manutencao12.mp4
ffmpeg -i manutencao14.mov -c:v libx264 -c:a aac -b:v 1M -b:a 128k manutencao14.mp4
```

### Opção 3: HandBrake (Interface Gráfica)
1. Baixe: https://handbrake.fr/
2. Abra os arquivos .mov
3. Configure:
   - **Preset:** Fast 720p30
   - **Format:** MP4
   - **Video Codec:** H.264
   - **Audio Codec:** AAC

## Após a Conversão

### 1. Substitua os arquivos
- Coloque os novos arquivos .mp4 na pasta do site
- Mantenha os nomes: `manutencao2.mp4`, `manutencao6.mp4`, etc.

### 2. Atualize o HTML
Substitua as linhas com `<img>` por `<video>`:

```html
<!-- Antes -->
<img src="manutencao.jpg" alt="Serviço de Manutenção 2" loading="lazy">

<!-- Depois -->
<video autoplay muted loop playsinline loading="lazy">
    <source src="manutencao2.mp4" type="video/mp4">
    <img src="manutencao.jpg" alt="Serviço de Manutenção 2" loading="lazy">
</video>
```

### 3. Remova os indicadores de vídeo
Após converter, remova as divs:
```html
<div class="video-indicator">
    <i class="fas fa-play-circle"></i>
    <span>Vídeo disponível</span>
</div>
```

## Configurações Recomendadas

### Para Web:
- **Resolução:** 720p (1280x720)
- **Bitrate:** 1-2 Mbps
- **FPS:** 30
- **Codec:** H.264
- **Audio:** AAC, 128kbps

### Tamanhos Esperados:
- `manutencao2.mov` (17MB) → `manutencao2.mp4` (~5MB)
- `manutencao6.mov` (323MB) → `manutencao6.mp4` (~15MB)
- `manutencao10.mov` (5.2MB) → `manutencao10.mp4` (~2MB)
- `manutencao12.mov` (12MB) → `manutencao12.mp4` (~4MB)
- `manutencao14.mov` (12MB) → `manutencao14.mp4` (~4MB)

## Benefícios da Conversão
- ✅ **Carregamento rápido** - arquivos menores
- ✅ **Compatibilidade** - funciona em todos os navegadores
- ✅ **Qualidade mantida** - visual adequado para web
- ✅ **SEO melhorado** - conteúdo otimizado

## Status Atual
- 🔄 **Aguardando conversão** - usando placeholders temporários
- ✅ **Design funcional** - indicadores visuais implementados
- ✅ **Responsivo** - funciona em mobile e desktop

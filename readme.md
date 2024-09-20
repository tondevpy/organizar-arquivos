# Organizador de Arquivos por Extensão

Este script Python organiza automaticamente os arquivos em um diretório, movendo-os para pastas nomeadas com base na extensão dos arquivos. Arquivos `.py` não serão movidos.

## Funcionalidades

- **Organização Automática**: O script percorre todos os arquivos do diretório atual onde é executado e os move para pastas nomeadas de acordo com a extensão do arquivo.
- **Exclusão de Arquivos `.py`**: Arquivos com a extensão `.py` não serão movidos, permanecendo no diretório original.
- **Criação Automática de Pastas**: Se não existir uma pasta para uma determinada extensão, o script criará automaticamente a pasta correspondente e moverá os arquivos para lá.

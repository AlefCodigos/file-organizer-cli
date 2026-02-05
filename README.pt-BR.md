# File Organizer CLI

Uma ferramenta de linha de comando para organizar arquivos em uma pasta em pastas separadas baseando-se no tipo dos arquivos.
Possui um modo de teste (dry-run) para simular a organização dos arquivos.

## Funcionalidades
- Organiza os arquivos por tipo (imagens, documentos, videos, etc)
- Modo de teste para simular a organização dos arquivos.
- Renomeia arquivos com nomes idênticos ao realizar a transferência (não deleta, não sobrescreve)

## Requisitos
- Python 3.x
- Pytest

## Uso
Na pasta organizer, rode:

```bash
python organizer.py -h
```

Exemplo:

```bash
python organizer.py --dry-run ./downloads
```

## Testes
Na pasta tests, rode:

```bash
pytest
```

Esse projeto foi projetado com o intuito de aprimoramento em Python, testagem e desenvolvimento de ferramentas de linha de comando.
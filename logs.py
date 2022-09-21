#!/usr/bin/env python3

import logging
import os

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)

# level
ch = logging.StreamHandler()
ch.setLevel(log_level)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# destino
log.addHandler(ch)


log.debug("Msg pro dev, qe, sysadmin")
log.info("Msg geral pro usuário")
log.warning("Aviso que não causa erro")
log.error("Erro que não afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")

print("-" * 20)

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
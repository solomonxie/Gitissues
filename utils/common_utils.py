# Copyright (c) 2022 data.ai inc. All rights reserved.

import os
import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def read_envfile(path: str) -> dict:
    pairs = {}
    p = Path(path)
    if not p.exists():
        return {}
    ptn = re.compile(r'[\'"]?([^\s#\'"]+)[\'"]?')
    lines = p.read_text().split('\n')
    for s in lines:
        if '=' not in s:
            continue
        s = s.strip()
        key = s[:s.index('=')]
        value = s[s.index('=')+1:]
        result = ptn.findall(value)
        value = result[0] if result else ''
        ignores = [
            key.startswith('#') or value.startswith('#'),
            key in [None, ''] or value in [None, ''],
            '-' in key,
            bool(re.search(r'^[0-9]', key)),
            value.startswith('"') and not value.endswith('"'),
            value.startswith("'") and not value.endswith("'"),
            # bool(value),  # Value is always a string
        ]
        if any(ignores):
            logger.debug(f'IGNORE ENV-V [{key}] FOR CHECKS: {ignores}')
            continue
        pairs[key] = value
    logger.info(f'OK: LOADED ENV VARS FROM [{path}]: {list(pairs.keys())}')
    return pairs


def inject_envfile(path: str) -> dict:
    pairs = read_envfile(path)
    for k, v in pairs.items():
        os.environ[k] = v
    return pairs


def main():
    inject_envfile('./envfile-local')


if __name__ == '__main__':
    main()

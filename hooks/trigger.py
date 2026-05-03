#!/usr/bin/env python3
"""
session-end hook trigger
Intercepts UserPromptSubmit events and injects context for session-end phrases.
"""
import json
import sys


def main():
    d = json.load(sys.stdin)
    msg = d.get('message', '') or ''
    msg_lower = msg.lower()

    if 'end session' in msg_lower or '结束对话' in msg:
        sm = (
            '[Session-End Triggered]\n\n'
            '<EXTREMELY_IMPORTANT>\n'
            'Invoke the session-end skill immediately. '
            'Do not say "sure" or "I will" — just invoke it.\n'
            '</EXTREMELY_IMPORTANT>'
        )
    else:
        sm = ''

    reminder = (
        '[Memory Rule] On mistake/correction → write feedback memory immediately. '
        'On phase complete → decide whether to update memory. Do not wait to be asked.'
    )

    output = '\n\n'.join(filter(None, [sm, reminder]))
    print(json.dumps({'systemMessage': output}, ensure_ascii=False))


if __name__ == '__main__':
    main()

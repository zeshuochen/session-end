#!/usr/bin/env python3
"""
session-end hook trigger
Intercepts UserPromptSubmit events and injects context for session lifecycle phrases.
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
    elif 'start session' in msg_lower or '开启对话' in msg:
        sm = (
            '[Session-Start Triggered]\n\n'
            '<EXTREMELY_IMPORTANT>\n'
            'Execute the following steps immediately, in order, before responding to anything else:\n'
            '(1) Read your memory index (MEMORY.md or equivalent); read topic files relevant to the current project.\n'
            '(2) Extract the next-session todo list from the last session-end.\n'
            '(3) Give a brief status summary: active projects and outstanding todos.\n'
            'Start immediately — do not say "sure" or "I will".\n'
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

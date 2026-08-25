#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILTER = ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt"
USERSCRIPT = ROOT / "UserScript" / "x-auto-select-following-latest-sort.user.js"

FILTER_VERSION = "202608251419"
RULE_COMMENT = '! ホーム上部の「おすすめ」タブを非表示'
RULE = 'x.com#?#div[role="presentation"]:has(> div[role="tab"] span:contains(/^おすすめ$/))'

text = FILTER.read_text(encoding="utf-8")
text = re.sub(r"^! Version: \d{12}$", f"! Version: {FILTER_VERSION}", text, count=1, flags=re.MULTILINE)
if RULE not in text:
    anchor = "! x.com\n"
    if anchor not in text:
        raise SystemExit("x.com section heading not found")
    text = text.replace(anchor, anchor + RULE_COMMENT + "\n" + RULE + "\n", 1)
FILTER.write_text(text, encoding="utf-8")

script = USERSCRIPT.read_text(encoding="utf-8")
script = script.replace("// @version      1.1.1", "// @version      1.2.0", 1)
script = script.replace(
    "// @description  Xのホームタイムラインで「並べ替え」メニューが開かれた際、自動的に「最新」を選択します。手動での変更も可能です。",
    "// @description  Xのホームで「フォロー中」を既定選択し、並べ替えメニューでは自動的に「最新」を選択します。",
    1,
)

if "const selectFollowingTab = () =>" not in script:
    anchor = "    let frameId = 0;\n"
    addition = r'''
    let followingFrameId = 0;
    let lastPathname = location.pathname;
    let followingSelectionRequested = false;

    const selectFollowingTab = () => {
        followingFrameId = 0;

        if (location.pathname !== lastPathname) {
            lastPathname = location.pathname;
            followingSelectionRequested = false;
        }
        if (location.pathname !== '/home') return;

        for (const tab of document.querySelectorAll('[role="tab"]')) {
            const label = (tab.textContent || '').trim();
            if (label !== 'フォロー中' && label !== 'Following') continue;

            if (tab.getAttribute('aria-selected') === 'true') {
                followingSelectionRequested = true;
                return;
            }
            if (!followingSelectionRequested && tab.isConnected) {
                followingSelectionRequested = true;
                tab.click();
            }
            return;
        }
    };

    const queueFollowingTabSelection = () => {
        if (!followingFrameId) {
            followingFrameId = requestAnimationFrame(selectFollowingTab);
        }
    };
'''
    if anchor not in script:
        raise SystemExit("UserScript state anchor not found")
    script = script.replace(anchor, anchor + addition, 1)

    old_observer = r'''    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            for (const node of mutation.addedNodes) {
                inspectAddedNode(node);
            }
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
})();
'''
    new_observer = r'''    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            for (const node of mutation.addedNodes) {
                inspectAddedNode(node);
            }
        }
        queueFollowingTabSelection();
    });

    observer.observe(document.body, { childList: true, subtree: true });
    queueFollowingTabSelection();
})();
'''
    if old_observer not in script:
        raise SystemExit("UserScript observer anchor not found")
    script = script.replace(old_observer, new_observer, 1)

USERSCRIPT.write_text(script, encoding="utf-8")

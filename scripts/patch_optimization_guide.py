#!/usr/bin/env python3
"""One-off, fail-closed corrections for the optimization guide.

Every replacement must match exactly once. The file is written only after all
checks pass, so upstream text changes cannot cause a partial or broad rewrite.
"""

from pathlib import Path
import re

PATH = Path("Markdown Notes/ChromeOS & Android Optimization Guide.md")
text = PATH.read_text(encoding="utf-8")
original = text


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected exactly one match, got {count}: {old[:80]!r}")
    text = text.replace(old, new, 1)


def regex_once(pattern: str, replacement: str) -> None:
    global text
    text, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"expected exactly one regex match, got {count}: {pattern[:80]!r}")


replace_once("| **Version** | 20260825 |", "| **Version** | 20260908 |")

replace_once(
    "Googleの多くのサービスでは、年額サブスクリプションを「月額 × 約10か月分」の料金で提供しており、割安になります。\n"
    "ただし、年額サブスクリプションは一度支払うと、契約期間の途中で解約しても日割り計算による払い戻しは行われません。",
    "一部のサブスクリプションでは月額プランより割安な年額プランが用意されていますが、割引率、途中解約、払い戻しの条件はサービスごとに異なります。契約前に、公式の料金ページと解約・返金条件を個別に確認します。"
)

replace_once(
    "なお、ahamo回線契約者は基本的にdocomoのサポートを受けることができません。",
    "docomo経由で契約したサービスの問い合わせ先やサポート範囲は、契約内容と窓口によって異なります。ahamoを含め、一律にサポート不可とは判断せず、対象サービスの公式窓口案内を確認します。"
)

replace_once(
    "これらの不具合の多くは、複数の契約がGoogle One メンバーシップ上で重複し、システムが矛盾した状態に陥ることが原因と考えられます。Google One メンバーシップの重複を整理した後、時間の経過をおいても、それで全ての不具合が直るかどうかは分かりません。\n\n"
    "**❗️いずれにしろ、Google One メンバーシップに適用する購入特典や有料プランは1つに限定するべきです。**",
    "この事例では複数の購入特典・有料プランを重ねた後に不具合が発生しましたが、Googleが一般的な原因として『契約の重複』を公表していることまでは確認できていません。再発防止のため、自分の環境では新しい特典やプランを有効化する前に、既存プランとの併用可否、切り替え条件、残存期間の扱いを公式ページまたはサポートで確認します。"
)

regex_once(
    r"\*\*Google One メンバーシップ・不具合解決の最終手段\*\*\n\n.*?\n\n\* \*\*参考サイト\*\*： \[r/GoogleOne｜Reddit\]",
    "**Google Oneの契約を整理する場合**\n\n通常は、まずGoogle Oneのプラン変更・解約手順と、購入元がGoogle Play / App Store / 携帯通信事業者などの第三者かを確認します。第三者経由の契約は、その提供元で管理が必要な場合があります。\n\nGoogle公式ヘルプには、特定の契約移行や解約状況でGoogle Oneサービス自体を削除する手順もありますが、一般的な『不具合の初期化』として常用する操作ではありません。Google Oneサービスを削除するとプラン関連データや設定等に影響するため、実行前に公式ヘルプとサポートで影響範囲を確認します。Google Drive、Gmail、Googleフォトの保存ファイルが操作直後に一括削除される、という意味ではありません。\n\n* **参考サイト**： [r/GoogleOne｜Reddit]"
)

# Chrome theme section was removed from this repository's intended scope.
regex_once(
    r"\n---\n\n## ChromeOS Chrome テーマ\n.*?\n---\n\n## ChromeOS Chrome アプリ",
    "\n---\n\n## ChromeOS Chrome アプリ"
)

replace_once(
    "**[Buster: Captcha Solver for Humans](https://chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl)**：音声認証とAIを活用してreCAPTCHAを自動で突破する。",
    "**[Buster: Captcha Solver for Humans](https://chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl)**：音声チャレンジを利用してCAPTCHAの解答を支援する拡張機能。対象サービスの利用規約や仕様変更により利用できない場合があります。"
)

regex_once(
    r"\*\*注意が必要な特殊な電話番号\*\*\n1\. `\+` で始まる.*?6\. `0180-` → 情報料として通話料とは別に料金が発生します。",
    "**電話番号表示だけで相手を信用しない**\n\n警察庁は、実在する警察署等の電話番号を偽装して表示させる手口を確認しています。末尾が`0110`であることや、日本の国番号`+81`を含むことだけで、本物・詐欺のどちらとも判定できません。警察官を名乗る電話で捜査対象などと言われた場合は一度電話を切り、相手が名乗った所属・氏名を控えたうえで、自分で調べた警察署の公式番号または警察相談専用電話`#9110`へ確認します。\n\n`0120` / `0800`、`050`なども正規の企業・サービスで広く使われています。番号種別だけを詐欺判定に使わず、金銭、暗証番号、認証コード、遠隔操作アプリの導入などを要求された場合は特に慎重に確認します。"
)

replace_once(
    "ブラウジング中にコンテンツブロッカーを使うことで、特殊詐欺に遭う確率を大幅に下げることができるので、多層防御の1つに加えてもよいかと思います。個人的に特殊詐欺に遭う確率を最小限に抑えることを最優先事項にしているので、広告を非表示にするサブスクリプションの利用も考慮しています。",
    "コンテンツブロッカーは、一部の悪質広告、既知の不正ドメイン、不要なリダイレクトへの接触機会を減らす補助策にはなりますが、フィッシングや特殊詐欺そのものを防げる保証はありません。OS・ブラウザの更新、パスワードマネージャー、パスキーや多要素認証、公式アプリ・ブックマークからのアクセス、電話やメッセージ内容の独立確認と組み合わせます。"
)

replace_once(
    "* **[uBlock Origin – Badware risks](https://github.com/uBlockOrigin/uAssets)**：Yuki2718氏がフィルタの監修に関わっています。",
    "* **[uBlock Origin – Badware risks](https://github.com/uBlockOrigin/uAssets)**：uBlock Originの公式uAssetsで管理される悪質サイト対策用フィルタ。個々のルールの作者・レビュー担当は公開履歴で確認します。"
)
replace_once(
    "* **[AdGuard Japanese filter Plus](https://github.com/Yuki2718/adblock2)**：Yuki2718氏自身がフィルタの監修をしています。",
    "* **[AdGuard Japanese filter Plus](https://github.com/Yuki2718/adblock2)**：Yuki2718氏の公開リポジトリでメンテナンスされている追加フィルタ。"
)

regex_once(
    r"AdGuard ブラウザ拡張機能 MV3対応版でスクリプトレットを含む高度なルールを使用する場合は、.*?`! Version:` は版の識別と更新状況の確認に有用ですが、URLの再取得そのものを成立させる唯一の条件ではありません。",
    "AdGuard ブラウザ拡張機能 MV3では、Custom filtersやJavaScriptを必要とするユーザールールのためにChromeのUser Scripts APIを使用します。AdGuard公式によると、Chrome 138以降では `chrome://extensions` > AdGuard > 詳細から **ユーザースクリプトを許可する** を有効にします。Chrome 138未満ではデベロッパーモードが必要です。\n\nv5.2系でMV3版へCustom filtersが再導入され、v5.4.1.3ではCustom filtersが拡張機能本体の更新とは独立して再び更新できるようになりました。組み込みフィルタとURL購読のCustom filtersでは更新経路が異なるため、同じ仕組みとして扱いません。`! Version:` はフィルタ版の識別には有用ですが、URL再取得の唯一の成立条件ではありません。"
)

regex_once(
    r"\*\*Web版YouTubeについての留意点\*\*\n\nYouTube Anti-Adblock回避ルールは、.*?\(\[Issues #27415\].*?\)\.\n",
    "**Web版YouTubeについての留意点**\n\nYouTubeの広告配信やアンチ広告ブロック対策は頻繁に変更されます。問題報告時は、各プロジェクトの公式案内に従い、フィルタを最新化したうえで、追加フィルタ・UserScript・他のブロッカーを一時的に外して再現性を確認します。特定の開発者の所属、レビュー、承認関係は、本人またはプロジェクトが公開した資料で確認できる範囲を超えて推測しません。\n"
)

replace_once(
    "※ 実態はDNSブロッカーのため、ABP形式の構文（`||example.com^`）には対応していません。",
    "※ ダウンロードするブロックリストはhosts / domains-only系の単純な形式を使用します。`additionalHosts.txt`では`!`によるホワイトリスト、`*`ワイルドカード、`>`によるカスタムIP指定など独自の追加構文を利用できますが、Adblock Plus形式の`||example.com^` / `@@||example.com^`とは別の構文です。"
)

replace_once(
    "Android版Chromeなどで高精度なブロックを行うには必須です。暗号化通信を一時解析し、要素をブロックします。Personal CA証明書のインストールが必要です。",
    "HTTPSサイトや対応アプリの暗号化通信を内容まで検査して、ネットワークルール、要素隠蔽、スクリプトレット等を十分に適用するにはHTTPSフィルタリングが重要です。AdGuardは端末内で通信を復号・検査して再暗号化するため、ユーザーCA証明書のインストールが必要です。HTTPSフィルタリングを無効にしてもDNSフィルタリングや一部のネットワーク遮断まで全て無効になるわけではありませんが、暗号化された通信内容を利用する高度な処理は制限されます。"
)

regex_once(
    r" HTTPSフィルタリングの有効化は、AdGuard社への根本的な信頼が前提となります.*?\n\n\*\*ローカルVPNによる監視を行わず",
    " HTTPSフィルタリングでは端末にAdGuardのCA証明書を信頼させるため、製品と証明書管理を信頼できることが前提です。AdGuardにはHTTPSフィルタリング対象外のサイト・アプリがあり、アプリ側がユーザーCAを信頼しない場合もあります。金融・決済などの高感度な通信で問題が起きた場合は、無理に証明書を適用せず、公式のHTTPS除外設定とアプリ側の証明書要件を確認します。\n\n**ローカルVPNによる監視を行わず"
)

regex_once(
    r"\*\*DNSサーバー & ChromeOS追加設定\*\*\n\nAdGuard内でDNSを設定します.*?\* \*\*フィルタ自動更新不可\*\*：ホーム画面の↻を手動タップ。",
    "**DNSサーバー設定**\n\nDNSリゾルバは、必要な暗号化方式、プライバシーポリシー、可用性、速度を基準に選びます。Google Public DNSは選択肢の一つですが、一律の推奨とはしません。AdGuard for AndroidのDNS保護を利用する場合は、Android/ChromeOS側のネームサーバー変更を追加すると経路が複雑になるため、目的と実際の問い合わせ経路をログで確認します。\n\n**トラブルシューティング**\n* **Wi-Fi接続不良**：IPv6フィルタリングを一律に無効化しません。AdGuardを停止した場合との比較、Filtering log、IPv4/IPv6の接続状況を確認し、IPv6との関連が再現できた場合だけ診断目的で変更し、改善しなければ元に戻します。\n* **フィルタ更新の確認**：自動更新が疑わしい場合は、使用中バージョンのUIから手動更新を実行して切り分けます。表示される導線はバージョンにより変わるため、固定のボタン位置は公式ヘルプと実画面で確認します。"
)

# Remove unsupported claim that Device Administrator prevents task killing.
regex_once(
    r"\*\*Android 17の「デバイスの管理」を有効化（Pixel 10aで確認）\*\*\n\nAndroid 17では、.*?ただし、「VPN以外の接続をブロック」を有効にすると、AdGuard停止時やVPN接続失敗時に通信できなくなる点に注意してください。",
    "**Android 17 / Pixelでの常駐設定**\n\nAndroid 17だからという理由だけで、AdGuardを『デバイス管理』へ登録するとタスクキルを防げるという一般仕様は、Android DevelopersまたはAdGuard公式資料から確認できませんでした。この設定を常駐対策として必須扱いしません。\n\nバックグラウンド停止が問題になる場合は、AdGuard公式のメーカー別ガイドに沿ってバッテリーのバックグラウンド制限を確認し、Androidの **常時接続VPN** を利用します。**VPN以外の接続をブロック** は、VPN停止時にも通信を許可しないfail-closed機能であり、常駐性を高める機能ではありません。必要な通信ポリシーを理解した場合だけ有効にします。Android 17にはアプリのメモリ制限もあるため、停止原因はログを確認して切り分けます。"
)

replace_once(
    "③ **MacroDroidを利用したVPN自動再接続タスクの作成**（最も効果的）",
    "③ **MacroDroidを利用したVPN自動再接続タスクの作成**（個人環境での復帰補助ワークアラウンド）"
)
replace_once(
    "* WebViewの影響は v4.10 以降で修正されました。OSによるタスクキル問題は常時接続VPNの有効化やMacroDroidの導入で対処します。（[タスクキル対策ガイド](https://adguard.com/kb/ja/adguard-for-android/solving-problems/background-work/)）",
    "* WebView関連の既知問題は v4.10系で修正されています。バックグラウンド停止については、まずAdGuard公式のメーカー別タスクキル対策と常時接続VPNを確認します。MacroDroidは公式の必須手順ではなく、自分の環境で必要性と副作用を確認して使う補助策です。（[タスクキル対策ガイド](https://adguard.com/kb/ja/adguard-for-android/solving-problems/background-work/)）"
)

replace_once(
    "スマートフォンの「プライベートDNS」設定に特定のホスト名を入力するだけで、端末全体に表示される広告を非表示にすることができます。",
    "スマートフォンの「プライベートDNS」へ広告・トラッカー遮断を行うDNSサービスのホスト名を設定すると、DNSで識別できる対象ドメインへの接続を端末全体で遮断できます。同一ドメインから配信される広告、ページ内要素、URLパス単位の広告などはDNSだけでは除去できません。"
)
replace_once(
    "* 入力欄に以下のホスト名を入力して保存します。現在はより安定している**新バージョン**の入力が推奨されています。\n  \n    * **新バージョン（推奨）**：`dns.adguard-dns.com`\n    * **旧バージョン** ：`dns.adguard.com`",
    "* AdGuardのパブリックDNSを使う場合、AdGuard公式が現在案内しているデフォルトサーバーのホスト名は `dns.adguard-dns.com` です。過去のホスト名を『旧版』として併記して常用せず、公式の接続ページに掲載されている現在の値を使用します。"
)

regex_once(
    r"## Aluminium OS / Googlebook / Linux\n.*?\n\*\*Linux 関連\*\*",
    "## Googlebook / Aluminium / Linux\nGoogleは2026年5月に新しいノートPCカテゴリ **Googlebook** を発表しました。公式説明では、AndroidとChromeOSの長所を組み合わせ、Android tech stackの一部を基盤とする製品とされています。Acer、ASUS、Dell、HP、Lenovoが初期パートナーとして公表され、2026年秋の提供開始が予告されています。\n\n`Aluminium`は、発表前の求人情報などから報道されたAndroidベースPCプロジェクトのコードネームです。Googleは製品発表で『Aluminium OS』または『ALOS』を正式名称として使用していません。このため、Googlebookが『Aluminium OSを搭載する』、ChromeOSが特定年に終了する、既存ChromebookがGooglebook系OSへ移行するといった未発表事項は確定情報として扱いません。\n\n詳細は [Googlebook / Aluminium 調査レポート](Googlebook%20%26%20Aluminium%20Survey%20Report%20-%20Revised%20Edition.md) に分離して記録します。\n\n**公式情報**\n* [Introducing Googlebook, designed for Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/)\n* [The Android Show: I/O Edition 2026（Google Japan）](https://blog.google/intl/ja-jp/products/android-chrome-play/android-show-io-edition-2026/)\n* [Chromebookの自動更新ポリシー](https://support.google.com/chrome/a/answer/6220366?hl=ja)\n\n**Linux 関連**"
)

if text == original:
    raise RuntimeError("no changes made")
PATH.write_text(text, encoding="utf-8")
print("Optimization guide corrections applied successfully.")

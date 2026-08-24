# Designing AdGuard Custom Rules

AdGuardカスタムルールを設計・検証する際の最小限の指針です。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## 基本方針

AdGuardのルールは、使用する製品ごとに対応機能が異なります。ブラウザ拡張機能、AdGuard for Android、AdGuard for Windowsなどで同じ構文が常に同じように利用できるとは限りません。

ルールを書く前に、対象製品の公式構文リファレンスと製品ドキュメントを確認します。

## 設計の流れ

1. フィルタリングログやブラウザ開発者ツールで、対象となる通信またはDOM要素を確認します。
2. ネットワークルールで遮断するのか、要素隠蔽ルールで表示だけを除去するのかを分けます。
3. できるだけ対象範囲を限定したルールを作成します。
4. 既存フィルタとの重複や例外ルールの必要性を確認します。
5. 対象サイトの主要機能が壊れていないか再検証します。

## MV3ブラウザ拡張機能

Manifest V3のブラウザ拡張機能では、ネットワークルールの一部がChromeのDeclarative Net Request APIに変換されます。変換できないルールや、製品側で制限される構文があります。

- [Chrome — Declarative Net Request API](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest)
- [AdGuard — MV3 browser extension](https://adguard.com/kb/adguard-browser-extension/mv3-version/)

## AdGuard for Android

AdGuard for AndroidはローカルVPNを利用して端末のトラフィックをフィルタリングし、HTTPSフィルタリングを有効にした場合はHTTPS通信も処理できます。アプリ単位のフィルタリングやDNS保護など、ブラウザ拡張機能とは異なる機能があります。

- [AdGuard for Android overview](https://adguard.com/kb/adguard-for-android/overview/)
- [HTTPS filtering](https://adguard.com/kb/general/https-filtering/what-is-https-filtering/)

## ルール構文

構文の詳細は本書で再掲せず、公式リファレンスを正本とします。

- [AdGuard — How to create your own ad filters](https://adguard.com/kb/general/ad-filtering/create-own-filters/)

主要構文の簡易一覧は[`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)を参照してください。

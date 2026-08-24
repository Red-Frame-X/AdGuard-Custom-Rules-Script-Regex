# ChromeOS & Android Optimization Guide

ChromeOSとAndroidの設定・運用について、公式ドキュメントで確認できる内容に限定した簡易ガイドです。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## ChromeOS

### OSアップデート

ChromeOSの更新は、Googleが案内する設定画面から実行します。

1. Chromebookをインターネットへ接続します。
2. **設定**を開きます。
3. **ChromeOSについて**を開きます。
4. **アップデートを確認**を選択します。
5. 必要に応じて再起動します。

- [Chromebookを更新する](https://support.google.com/chromebook/answer/15468740?hl=ja)
- [Chromebookの自動更新ポリシー](https://support.google.com/chrome/a/answer/6220366?hl=ja)

### Chrome拡張機能

Manifest V2拡張機能はChromeで段階的に無効化され、Manifest V3への移行が進められています。

- [Manifest V2 support timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)
- [Chrome Web Store](https://chromewebstore.google.com/category/extensions)

拡張機能を多数導入すると競合が発生する可能性があるため、不具合時は拡張機能を個別に無効化して切り分けます。

## Android

### アプリ権限

Androidでは、アプリごとにカメラ、マイク、位置情報などの権限を管理できます。不要な権限は設定画面から見直します。

- [Change app permissions on your Android phone](https://support.google.com/android/answer/9431959)

### バッテリー

Androidでは、アプリごとにバッテリー使用状況を確認し、バックグラウンド利用を制御できます。設定名称は端末メーカーやAndroidバージョンで異なる場合があります。

- [Check battery life and use](https://support.google.com/android/answer/7664692)

### Private DNS

AndroidはPrivate DNSをサポートしています。設定できるのはDNS-over-TLS対応プロバイダーです。

- [Manage advanced network settings on your Android phone](https://support.google.com/android/answer/9654714)

## コンテンツブロック

AdGuard Browser ExtensionのManifest V3版はChromeのDeclarative Net Request APIを利用します。AdGuard for AndroidはローカルVPNを利用して端末トラフィックをフィルタリングします。両者は実行環境と対応機能が異なります。

- [AdGuard Browser Extension MV3](https://adguard.com/kb/adguard-browser-extension/mv3-version/)
- [AdGuard for Android overview](https://adguard.com/kb/adguard-for-android/overview/)
- [AdGuard filtering syntax](https://adguard.com/kb/general/ad-filtering/create-own-filters/)

詳細なカスタムルールは[`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)を参照してください。

## GitHub連携

GitHub上のコード、Issue、Pull Request、Actionsなどの仕様はGitHub Docsを確認してください。

- [GitHub Docs](https://docs.github.com/)

## この文書から削除した内容

個人のサブスクリプション一覧、個別サービスの障害推測、Reddit上の体験談、特定拡張機能が原因とする未確認の推測、発売前製品の予測、公式根拠のない最適化値や「必須」「最適」と断定した設定は削除しました。

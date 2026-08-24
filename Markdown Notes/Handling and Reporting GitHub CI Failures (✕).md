# Handling and Reporting GitHub CI Failures (✕)

GitHubのステータスチェック失敗を確認するための簡潔なメモです。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## ステータスチェック

GitHubでは、プルリクエストやコミットに対してChecks APIやCommit Status APIから状態が報告されます。`failure`、`error`、`timed_out`、`cancelled`など、失敗系の状態が付くとチェックが成功していないことを確認できます。

`Verified` / `Unverified` はコミット署名の検証状態であり、CIのステータスチェックとは別の機能です。

## 確認手順

1. 対象のコミットまたはプルリクエストで失敗したチェックを開きます。
2. GitHub Actionsの場合は該当Workflow runとJobのログを確認します。
3. ログに表示された失敗ステップ、終了コード、エラーメッセージを確認します。
4. 原因を修正した後、必要に応じて再実行または新しいコミットで再検証します。

## 報告時に含める情報

IssueやプルリクエストでCI失敗を共有する場合は、少なくとも次の情報があると確認しやすくなります。

- 対象コミットSHAまたはPR番号
- 失敗したWorkflow / Job名
- Workflow runへのリンク
- エラーログの該当部分
- 再現条件が分かる場合はその手順

## 公式ドキュメント

- [About status checks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
- [REST API endpoints for commit statuses](https://docs.github.com/rest/commits/statuses)
- [REST API endpoints for check runs](https://docs.github.com/rest/checks/runs)
- [About commit signature verification](https://docs.github.com/authentication/managing-commit-signature-verification/about-commit-signature-verification)

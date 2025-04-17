import sys
import markdown

def convert_markdown_to_html(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()

        html = markdown.markdown(markdown_text)

        with open(output_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html)

        print(f"✅ 変換完了！{output_path} に保存しました。")

    except FileNotFoundError:
        print(f"❌ 入力ファイルが見つかりません: {input_path}")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")


def main():
    if len(sys.argv) != 4:
        print("使用方法: python3 file-converter.py markdown inputfile outputfile")
        return

    command = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]

    if command != "markdown":
        print("❌ 未対応のコマンドです。対応コマンド: markdown")
        return

    convert_markdown_to_html(inputfile, outputfile)


if __name__ == "__main__":
    main()

import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import threading
import gc

# 遅延インポート - 必要時まで重いライブラリを読み込まない
def import_image_libs():
    """画像処理ライブラリを遅延インポート（最小限）"""
    global Image
    # PILの最小限の機能のみインポート
    from PIL import Image

# 多言語対応の辞書
translations = {
    "ja": {
        "title": "NotDotBlur",
        "main_title": "NotDotBlur",
        "scale_label": "拡大倍率:",
        "select_button": "画像を選択",
        "select_file_title": "画像ファイルを選択",
        "save_file_title": "拡大画像の保存先を選択",
        "error_invalid_scale": "倍率には1以上の整数を入力してください。",
        "error_scale_min": "倍率は1以上である必要があります",
        "info_supported_formats": "PNG、JPG、JPEG、GIF、BMPファイルをサポートしています",
        "success_saved": "拡大画像を保存しました:",
        "image_size": "画像サイズ:",
        "pixel_array_shape": "ピクセル配列の形状:",
        "pixel_data_type": "ピクセルデータ型:",
        "loading": "読み込み中..."
    },
    "en": {
        "title": "NotDotBlur",
        "main_title": "NotDotBlur",
        "scale_label": "Scale Factor:",
        "select_button": "Select Image",
        "select_file_title": "Select Image File",
        "save_file_title": "Select Save Location",
        "error_invalid_scale": "Please enter an integer of 1 or greater for the scale factor.",
        "error_scale_min": "Scale factor must be 1 or greater",
        "info_supported_formats": "Supports PNG, JPG, JPEG, GIF, BMP files",
        "success_saved": "Enlarged image saved:",
        "image_size": "Image size:",
        "pixel_array_shape": "Pixel array shape:",
        "pixel_data_type": "Pixel data type:",
        "loading": "Loading..."
    }
}

# 現在の言語設定（デフォルトは日本語）
current_language = "ja"

# フォント変数（後で初期化）
FONT_TITLE = None
FONT_BUTTON = None
FONT_LABEL = None
FONT_INFO = None

def init_fonts():
    """フォントを初期化する関数"""
    global FONT_TITLE, FONT_BUTTON, FONT_LABEL, FONT_INFO
    FONT_TITLE = ctk.CTkFont(family="メイリオ", size=24, weight="bold")
    FONT_BUTTON = ctk.CTkFont(size=16, weight="bold", family="メイリオ")
    FONT_LABEL = ctk.CTkFont(size=14)
    FONT_INFO = ctk.CTkFont(size=12, family="メイリオ")

def get_text(key):
    """指定されたキーのテキストを現在の言語で取得"""
    return translations[current_language].get(key, key)

def change_language(lang):
    """言語を変更する関数"""
    global current_language
    current_language = lang
    update_ui_texts()

def update_ui_texts():
    """UIのテキストを現在の言語に更新"""
    root.title(get_text("title"))
    title_label.configure(text=get_text("main_title"))
    scale_label.configure(text=get_text("scale_label"))
    select_button.configure(text=get_text("select_button"))
    info_label.configure(text=get_text("info_supported_formats"))

# CustomTkinterのテーマ設定（起動時に一度だけ実行）
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def enlarge_image_optimized(img, scale):
    """最適化された画像拡大処理（最小限のライブラリ使用）"""
    width, height = img.size
    new_width = width * scale
    new_height = height * scale
    
    # 新しい画像を作成
    enlarged_img = Image.new(img.mode, (new_width, new_height))
    
    # データを取得（効率的な方法）
    img_data = list(img.getdata())
    
    # 行ごとに処理（メモリ効率を考慮）
    for y in range(height):
        row_start = y * width
        for x in range(width):
            pixel = img_data[row_start + x]
            # 拡大された領域に同じピクセルを設定
            for dy in range(scale):
                for dx in range(scale):
                    enlarged_img.putpixel((x * scale + dx, y * scale + dy), pixel)
    
    return enlarged_img

def select_image():
    # 画像処理ライブラリを遅延インポート
    import_image_libs()
    
    file_path = filedialog.askopenfilename(
        title=get_text("select_file_title"),
        filetypes=[
            ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")
        ]
    )
    
    if file_path:
        img = Image.open(file_path).convert("RGBA")
        print(f"{get_text('image_size')} {img.size}")
        print(f"{get_text('pixel_array_shape')} {img.size[0]}x{img.size[1]}x4")
        print(f"{get_text('pixel_data_type')} uint8")

        # 倍率の取得と検証
        scale_input = scale_var.get().strip()
        try:
            scale = int(scale_input)
            if scale < 1:
                raise ValueError(get_text("error_scale_min"))
        except ValueError as e:
            if str(e) == get_text("error_scale_min"):
                messagebox.showerror("エラー", str(e))
            else:
                messagebox.showerror("エラー", get_text("error_invalid_scale"))
            return

        # --- ここから拡大処理（最適化版） ---
        print("画像拡大処理を開始...")
        enlarged_img = enlarge_image_optimized(img, scale)
        # --- ここまで拡大処理 ---
        
        save_path = filedialog.asksaveasfilename(
            title=get_text("save_file_title"),
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if save_path:
            enlarged_img.save(save_path)
            print(f"{get_text('success_saved')} {save_path}")

def show_splash_screen():
    """スプラッシュスクリーンを表示"""
    splash = ctk.CTk()
    splash.title("")
    splash.geometry("300x150")
    splash.resizable(False, False)
    splash.attributes('-topmost', True)
    
    # スプラッシュスクリーンを中央に配置
    splash.update_idletasks()
    x = (splash.winfo_screenwidth() // 2) - 150
    y = (splash.winfo_screenheight() // 2) - 75
    splash.geometry(f"300x150+{x}+{y}")
    
    # スプラッシュコンテンツ
    frame = ctk.CTkFrame(splash)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # フォントが初期化されていない場合はデフォルトフォントを使用
    title_font = FONT_TITLE if FONT_TITLE else ctk.CTkFont(size=24, weight="bold")
    info_font = FONT_INFO if FONT_INFO else ctk.CTkFont(size=12)
    
    title = ctk.CTkLabel(frame, text="NotDotBlur", font=title_font)
    title.pack(pady=(20, 10))
    
    loading = ctk.CTkLabel(frame, text=get_text("loading"), font=info_font)
    loading.pack(pady=10)
    
    splash.update()
    return splash

def create_ui():
    """UI要素を作成する関数"""
    global root, title_label, scale_label, select_button, info_label, scale_var
    
    # フォントを初期化
    init_fonts()
    
    # メインウィンドウの作成
    root = ctk.CTk()
    root.title(get_text("title"))
    root.geometry("600x400")
    root.resizable(False, False)
    
    # ウィンドウを中央に配置
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - 300
    y = (root.winfo_screenheight() // 2) - 200
    root.geometry(f"600x400+{x}+{y}")

    # アイコン設定
    def set_icon():
        try:
            if os.path.exists("favicon.ico"):
                root.iconbitmap("favicon.ico")
        except Exception as e:
            pass
    
    # アイコン設定を非同期で実行
    root.after(1000, set_icon)

    # メインフレーム
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # 言語切り替えボタン
    language_frame = ctk.CTkFrame(main_frame)
    language_frame.pack(fill="x", padx=20, pady=(10, 0))

    ja_button = ctk.CTkButton(
        language_frame,
        text="日本語",
        command=lambda: change_language("ja"),
        font=FONT_BUTTON,
        width=80,
        height=30
    )
    ja_button.pack(side="left", padx=(10, 5), pady=10)

    en_button = ctk.CTkButton(
        language_frame,
        text="English(US)",
        command=lambda: change_language("en"),
        width=80,
        height=30
    )
    en_button.pack(side="left", padx=5, pady=10)

    # タイトルラベル
    title_label = ctk.CTkLabel(
        main_frame, 
        text=get_text("main_title"), 
        font=FONT_TITLE
    )
    title_label.pack(pady=(20, 15))

    # 設定フレーム
    settings_frame = ctk.CTkFrame(main_frame)
    settings_frame.pack(fill="x", padx=20, pady=5)

    # 倍率設定
    scale_label = ctk.CTkLabel(settings_frame, text=get_text("scale_label"), font=FONT_LABEL)
    scale_label.pack(anchor="w", padx=20, pady=(15, 5))

    scale_var = ctk.StringVar(value="16")
    scale_entry = ctk.CTkEntry(
        settings_frame, 
        textvariable=scale_var, 
        width=120,
        font=FONT_LABEL
    )
    scale_entry.pack(anchor="w", padx=20, pady=(0, 15))

    # ボタンフレーム
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(fill="x", padx=20, pady=20)

    # 画像選択ボタン
    select_button = ctk.CTkButton(
        button_frame,
        text=get_text("select_button"),
        command=select_image,
        font=FONT_BUTTON,
        height=50,
        corner_radius=10
    )
    select_button.pack(pady=20)

    # 情報ラベル
    info_label = ctk.CTkLabel(
        main_frame,
        text=get_text("info_supported_formats"),
        font=FONT_INFO,
        text_color="gray"
    )
    info_label.pack(pady=(0, 20))

def preload_libraries():
    """バックグラウンドでライブラリをプリロード"""
    try:
        import_image_libs()
        gc.collect()
    except:
        pass

def main():
    """メイン関数"""
    # スプラッシュスクリーンを表示
    splash = show_splash_screen()
    
    # バックグラウンドでライブラリをプリロード
    preload_thread = threading.Thread(target=preload_libraries, daemon=True)
    preload_thread.start()
    
    # 短い遅延でスプラッシュスクリーンを表示
    splash.after(500, lambda: None)
    splash.update()
    
    # UIを作成
    create_ui()
    
    # スプラッシュスクリーンを閉じる
    splash.destroy()
    
    # ガベージコレクションを実行
    gc.collect()
    
    # メインループを開始
    root.mainloop()

if __name__ == "__main__":
    main() 
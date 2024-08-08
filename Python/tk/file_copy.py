import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

class FileCopyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("File Copy Application")
        self.geometry("500x300")

        # Source and destination paths
        self.source_path = ctk.StringVar()
        self.destination_path = ctk.StringVar()

        # Source path
        ctk.CTkLabel(self, text="Source Path:").pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.source_path).pack(fill="x", padx=20)
        ctk.CTkButton(self, text="Browse", command=self.browse_source).pack(pady=5)

        # Destination path
        ctk.CTkLabel(self, text="Destination Path:").pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.destination_path).pack(fill="x", padx=20)
        ctk.CTkButton(self, text="Browse", command=self.browse_destination).pack(pady=5)

        # Options
        self.preserve_permissions = ctk.BooleanVar(value=True)
        self.preserve_times = ctk.BooleanVar(value=True)
        self.preserve_ownership = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(self, text="Preserve Permissions", variable=self.preserve_permissions).pack(pady=5)
        ctk.CTkCheckBox(self, text="Preserve Timestamps", variable=self.preserve_times).pack(pady=5)
        ctk.CTkCheckBox(self, text="Preserve Ownership", variable=self.preserve_ownership).pack(pady=5)

        # Copy button
        ctk.CTkButton(self, text="Copy Files", command=self.copy_files).pack(pady=20)

    def browse_source(self):
        directory = filedialog.askdirectory()
        if directory:
            self.source_path.set(directory)

    def browse_destination(self):
        directory = filedialog.askdirectory()
        if directory:
            self.destination_path.set(directory)

    def copy_files(self):
        source = self.source_path.get()
        destination = self.destination_path.get()

        if not source or not destination:
            messagebox.showerror("Error", "Please select both source and destination paths")
            return

        try:
            for root, dirs, files in os.walk(source):
                for name in files:
                    src_file = os.path.join(root, name)
                    dest_file = os.path.join(destination, os.path.relpath(src_file, source))

                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)

                    shutil.copy2(src_file, dest_file) if self.preserve_times.get() else shutil.copy(src_file, dest_file)
                    if self.preserve_permissions.get():
                        shutil.copystat(src_file, dest_file)
                    if self.preserve_ownership.get():
                        st = os.stat(src_file)
                        os.chown(dest_file, st.st_uid, st.st_gid)
            
            messagebox.showinfo("Success", "Files copied successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = FileCopyApp()
    app.mainloop()

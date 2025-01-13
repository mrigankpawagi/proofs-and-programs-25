import os
import shutil
import stat

def install_hooks():
    # Get the root directory (where .git is)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hooks_dir = os.path.join(root_dir, '.git', 'hooks')
    source_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Hooks to install
    hooks = ['pre-commit', 'post-checkout']
    
    for hook in hooks:
        src = os.path.join(source_dir, hook)
        dst = os.path.join(hooks_dir, hook)
        
        # Copy the hook file
        print(f"Installing {hook} hook...")
        shutil.copy2(src, dst)
        
        # Make it executable (equivalent to chmod +x)
        st = os.stat(dst)
        os.chmod(dst, st.st_mode | stat.S_IEXEC)
        
        print(f"Successfully installed {hook} hook")

if __name__ == "__main__":
    try:
        install_hooks()
        print("\nAll hooks installed successfully!")
    except Exception as e:
        print(f"Error installing hooks: {str(e)}")

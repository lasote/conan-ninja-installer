from conans import ConanFile, CMake, tools, ConfigureEnvironment
import os


class NinjaInstallerConan(ConanFile):
    name = "ninja_installer"
    version = "0.1"
    license = "MIT"
    url = "http://github.com/lasote/conan-ninja-installer"
    settings = {"os": ["Windows", "Linux", "Macos"], "arch": ["x86", "x86_64"]}
    options = {"version": ["1.7.1", "1.6.0", "1.5.3", "1.5.1", "1.4.0"]} # https://github.com/ninja-build/ninja/releases
    default_options = "version=1.7.1"
    build_policy = "missing"
    
    
    def build(self):
        zip_name = {"Windows": "ninja-win.zip",
                    "Linux": "ninja-linux.zip",
                    "Macos": "ninja-mac.zip"}[str(self.settings.os)]
        
        url = "https://github.com/ninja-build/ninja/releases/download/v%s/%s" % (self.options.version, zip_name)
        tools.download(url, "ninja.zip", verify=False)
        tools.unzip("ninja.zip")
        
    def package(self):
        if str(self.settings.os) in ["Linux", "Macos"]:
            self.copy("ninja", dst="bin/")
            self.run("chmod +x %s" % os.path.join(self.package_folder, "bin", "ninja"))
        else:
            self.copy("ninja.exe", dst="bin/")
    
    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

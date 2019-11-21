from conans import ConanFile, CMake, tools
import os

class JsondtoConan(ConanFile):
    name = "json-dto"
    version = "0.2.9.1"
    license = "BSD-3-Clause"
    author = "Stiffstream info@stiffstream.com"
    url = "https://github.com/Stiffstream/json_dto-conan"
    description = "A small header-only helper for converting data between json representation and c++ structs"
    topics = ("JSON", "DTO", "Serialization")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    source_subfolder = "json_dto"

    requires = "rapidjson/1.1.0@bincrafters/stable"

    def source(self):
        # https://github.com/Stiffstream/json_dto/archive/v.0.2.8.tar.gz
        source_url = "https://github.com/Stiffstream/json_dto/archive"
        tools.get("{0}/v.{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "json_dto-v." + self.version
        os.rename(extracted_dir, self.source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.definitions['JSON_DTO_INSTALL'] = True
        cmake.definitions['JSON_DTO_FIND_DEPS'] = False
        cmake.configure(source_folder = self.source_subfolder + "/dev/json_dto")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.hpp", dst="include/json_dto", src=self.source_subfolder + "/dev/json_dto")
        self.copy("license*", src=self.source_subfolder, dst="licenses", ignore_case=True, keep_path=False)

    def package_id(self):
        self.info.header_only()



#include <iostream>
#include <clang-c/Index.h>

void traverseAST(CXCursor cursor) {
    // Print information about the cursor (e.g., type, name)
    CXString name = clang_getCursorSpelling(cursor);
    CXCursorKind kind = clang_getCursorKind(cursor);

    std::cout << "Cursor kind: " << clang_getCursorKindSpelling(kind) << ", Name: " << clang_getCString(name) << std::endl;

    // Traverse children of the cursor
    clang_visitChildren(cursor, [](CXCursor child, CXCursor /* parent */, CXClientData /* client_data */) {
        traverseAST(child);
        return CXChildVisit_Continue;
    }, nullptr);
}

int main() {
    // Initialize libclang
    CXIndex index = clang_createIndex(0, 0);
    const char* file = "your_cpp_file.cpp";
    const char* args[] = {"-std=c++11"}; // Optional: compiler arguments

    // Parse the translation unit
    CXTranslationUnit tu = clang_parseTranslationUnit(index, file, args, 1, nullptr, 0, CXTranslationUnit_None);
    if (!tu) {
        std::cerr << "Error parsing translation unit!" << std::endl;
        return 1;
    }

    // Get the cursor for the translation unit
    CXCursor cursor = clang_getTranslationUnitCursor(tu);

    // Traverse the AST
    traverseAST(cursor);

    // Clean up libclang resources
    clang_disposeTranslationUnit(tu);
    clang_disposeIndex(index);

    return 0;
}

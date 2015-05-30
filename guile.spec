#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : guile
Version  : 2.0.11
Release  : 3
URL      : ftp://ftp.gnu.org/gnu/guile/guile-2.0.11.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/guile/guile-2.0.11.tar.gz
Summary  : GNU's Ubiquitous Intelligent Language for Extension (uninstalled)
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 LGPL-3.0
Requires: guile-bin
Requires: guile-lib
Requires: guile-data
Requires: guile-doc
BuildRequires : emacs
BuildRequires : gmp-dev
BuildRequires : libunistring-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(bdw-gc)
BuildRequires : pkgconfig(libffi)
BuildRequires : readline-dev
BuildRequires : sed
BuildRequires : texinfo

%description
This is version 2.0 of Guile, Project GNU's extension language library.
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

%package bin
Summary: bin components for the guile package.
Group: Binaries
Requires: guile-data

%description bin
bin components for the guile package.


%package data
Summary: data components for the guile package.
Group: Data

%description data
data components for the guile package.


%package dev
Summary: dev components for the guile package.
Group: Development
Requires: guile-lib
Requires: guile-bin
Requires: guile-data

%description dev
dev components for the guile package.


%package doc
Summary: doc components for the guile package.
Group: Documentation

%description doc
doc components for the guile package.


%package lib
Summary: lib components for the guile package.
Group: Libraries
Requires: guile-data

%description lib
lib components for the guile package.


%prep
%setup -q -n guile-2.0.11

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/guile/2.0/ccache/ice-9/and-let-star.go
/usr/lib64/guile/2.0/ccache/ice-9/binary-ports.go
/usr/lib64/guile/2.0/ccache/ice-9/boot-9.go
/usr/lib64/guile/2.0/ccache/ice-9/buffered-input.go
/usr/lib64/guile/2.0/ccache/ice-9/calling.go
/usr/lib64/guile/2.0/ccache/ice-9/channel.go
/usr/lib64/guile/2.0/ccache/ice-9/command-line.go
/usr/lib64/guile/2.0/ccache/ice-9/common-list.go
/usr/lib64/guile/2.0/ccache/ice-9/control.go
/usr/lib64/guile/2.0/ccache/ice-9/curried-definitions.go
/usr/lib64/guile/2.0/ccache/ice-9/debug.go
/usr/lib64/guile/2.0/ccache/ice-9/deprecated.go
/usr/lib64/guile/2.0/ccache/ice-9/documentation.go
/usr/lib64/guile/2.0/ccache/ice-9/eval-string.go
/usr/lib64/guile/2.0/ccache/ice-9/eval.go
/usr/lib64/guile/2.0/ccache/ice-9/expect.go
/usr/lib64/guile/2.0/ccache/ice-9/format.go
/usr/lib64/guile/2.0/ccache/ice-9/ftw.go
/usr/lib64/guile/2.0/ccache/ice-9/futures.go
/usr/lib64/guile/2.0/ccache/ice-9/gap-buffer.go
/usr/lib64/guile/2.0/ccache/ice-9/getopt-long.go
/usr/lib64/guile/2.0/ccache/ice-9/hash-table.go
/usr/lib64/guile/2.0/ccache/ice-9/hcons.go
/usr/lib64/guile/2.0/ccache/ice-9/history.go
/usr/lib64/guile/2.0/ccache/ice-9/i18n.go
/usr/lib64/guile/2.0/ccache/ice-9/iconv.go
/usr/lib64/guile/2.0/ccache/ice-9/lineio.go
/usr/lib64/guile/2.0/ccache/ice-9/list.go
/usr/lib64/guile/2.0/ccache/ice-9/local-eval.go
/usr/lib64/guile/2.0/ccache/ice-9/ls.go
/usr/lib64/guile/2.0/ccache/ice-9/mapping.go
/usr/lib64/guile/2.0/ccache/ice-9/match.go
/usr/lib64/guile/2.0/ccache/ice-9/networking.go
/usr/lib64/guile/2.0/ccache/ice-9/null.go
/usr/lib64/guile/2.0/ccache/ice-9/occam-channel.go
/usr/lib64/guile/2.0/ccache/ice-9/optargs.go
/usr/lib64/guile/2.0/ccache/ice-9/poe.go
/usr/lib64/guile/2.0/ccache/ice-9/poll.go
/usr/lib64/guile/2.0/ccache/ice-9/popen.go
/usr/lib64/guile/2.0/ccache/ice-9/posix.go
/usr/lib64/guile/2.0/ccache/ice-9/pretty-print.go
/usr/lib64/guile/2.0/ccache/ice-9/psyntax-pp.go
/usr/lib64/guile/2.0/ccache/ice-9/q.go
/usr/lib64/guile/2.0/ccache/ice-9/r4rs.go
/usr/lib64/guile/2.0/ccache/ice-9/r5rs.go
/usr/lib64/guile/2.0/ccache/ice-9/rdelim.go
/usr/lib64/guile/2.0/ccache/ice-9/readline.go
/usr/lib64/guile/2.0/ccache/ice-9/receive.go
/usr/lib64/guile/2.0/ccache/ice-9/regex.go
/usr/lib64/guile/2.0/ccache/ice-9/runq.go
/usr/lib64/guile/2.0/ccache/ice-9/rw.go
/usr/lib64/guile/2.0/ccache/ice-9/safe-r5rs.go
/usr/lib64/guile/2.0/ccache/ice-9/safe.go
/usr/lib64/guile/2.0/ccache/ice-9/save-stack.go
/usr/lib64/guile/2.0/ccache/ice-9/scm-style-repl.go
/usr/lib64/guile/2.0/ccache/ice-9/serialize.go
/usr/lib64/guile/2.0/ccache/ice-9/session.go
/usr/lib64/guile/2.0/ccache/ice-9/slib.go
/usr/lib64/guile/2.0/ccache/ice-9/stack-catch.go
/usr/lib64/guile/2.0/ccache/ice-9/streams.go
/usr/lib64/guile/2.0/ccache/ice-9/string-fun.go
/usr/lib64/guile/2.0/ccache/ice-9/syncase.go
/usr/lib64/guile/2.0/ccache/ice-9/threads.go
/usr/lib64/guile/2.0/ccache/ice-9/time.go
/usr/lib64/guile/2.0/ccache/ice-9/top-repl.go
/usr/lib64/guile/2.0/ccache/ice-9/vlist.go
/usr/lib64/guile/2.0/ccache/ice-9/weak-vector.go
/usr/lib64/guile/2.0/ccache/language/assembly.go
/usr/lib64/guile/2.0/ccache/language/assembly/compile-bytecode.go
/usr/lib64/guile/2.0/ccache/language/assembly/decompile-bytecode.go
/usr/lib64/guile/2.0/ccache/language/assembly/disassemble.go
/usr/lib64/guile/2.0/ccache/language/assembly/spec.go
/usr/lib64/guile/2.0/ccache/language/brainfuck/compile-scheme.go
/usr/lib64/guile/2.0/ccache/language/brainfuck/compile-tree-il.go
/usr/lib64/guile/2.0/ccache/language/brainfuck/parse.go
/usr/lib64/guile/2.0/ccache/language/brainfuck/spec.go
/usr/lib64/guile/2.0/ccache/language/bytecode/spec.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/array.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/base.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/compile-tree-il.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/function.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/impl.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/parse.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/spec.go
/usr/lib64/guile/2.0/ccache/language/ecmascript/tokenize.go
/usr/lib64/guile/2.0/ccache/language/elisp/bindings.go
/usr/lib64/guile/2.0/ccache/language/elisp/compile-tree-il.go
/usr/lib64/guile/2.0/ccache/language/elisp/lexer.go
/usr/lib64/guile/2.0/ccache/language/elisp/parser.go
/usr/lib64/guile/2.0/ccache/language/elisp/runtime.go
/usr/lib64/guile/2.0/ccache/language/elisp/runtime/function-slot.go
/usr/lib64/guile/2.0/ccache/language/elisp/runtime/macros.go
/usr/lib64/guile/2.0/ccache/language/elisp/runtime/subrs.go
/usr/lib64/guile/2.0/ccache/language/elisp/runtime/value-slot.go
/usr/lib64/guile/2.0/ccache/language/elisp/spec.go
/usr/lib64/guile/2.0/ccache/language/glil.go
/usr/lib64/guile/2.0/ccache/language/glil/compile-assembly.go
/usr/lib64/guile/2.0/ccache/language/glil/spec.go
/usr/lib64/guile/2.0/ccache/language/objcode/spec.go
/usr/lib64/guile/2.0/ccache/language/scheme/compile-tree-il.go
/usr/lib64/guile/2.0/ccache/language/scheme/decompile-tree-il.go
/usr/lib64/guile/2.0/ccache/language/scheme/spec.go
/usr/lib64/guile/2.0/ccache/language/tree-il.go
/usr/lib64/guile/2.0/ccache/language/tree-il/analyze.go
/usr/lib64/guile/2.0/ccache/language/tree-il/canonicalize.go
/usr/lib64/guile/2.0/ccache/language/tree-il/compile-glil.go
/usr/lib64/guile/2.0/ccache/language/tree-il/cse.go
/usr/lib64/guile/2.0/ccache/language/tree-il/debug.go
/usr/lib64/guile/2.0/ccache/language/tree-il/effects.go
/usr/lib64/guile/2.0/ccache/language/tree-il/fix-letrec.go
/usr/lib64/guile/2.0/ccache/language/tree-il/inline.go
/usr/lib64/guile/2.0/ccache/language/tree-il/optimize.go
/usr/lib64/guile/2.0/ccache/language/tree-il/peval.go
/usr/lib64/guile/2.0/ccache/language/tree-il/primitives.go
/usr/lib64/guile/2.0/ccache/language/tree-il/spec.go
/usr/lib64/guile/2.0/ccache/language/value/spec.go
/usr/lib64/guile/2.0/ccache/oop/goops.go
/usr/lib64/guile/2.0/ccache/oop/goops/accessors.go
/usr/lib64/guile/2.0/ccache/oop/goops/active-slot.go
/usr/lib64/guile/2.0/ccache/oop/goops/compile.go
/usr/lib64/guile/2.0/ccache/oop/goops/composite-slot.go
/usr/lib64/guile/2.0/ccache/oop/goops/describe.go
/usr/lib64/guile/2.0/ccache/oop/goops/dispatch.go
/usr/lib64/guile/2.0/ccache/oop/goops/internal.go
/usr/lib64/guile/2.0/ccache/oop/goops/save.go
/usr/lib64/guile/2.0/ccache/oop/goops/simple.go
/usr/lib64/guile/2.0/ccache/oop/goops/stklos.go
/usr/lib64/guile/2.0/ccache/oop/goops/util.go
/usr/lib64/guile/2.0/ccache/rnrs.go
/usr/lib64/guile/2.0/ccache/rnrs/arithmetic/bitwise.go
/usr/lib64/guile/2.0/ccache/rnrs/arithmetic/fixnums.go
/usr/lib64/guile/2.0/ccache/rnrs/arithmetic/flonums.go
/usr/lib64/guile/2.0/ccache/rnrs/base.go
/usr/lib64/guile/2.0/ccache/rnrs/bytevectors.go
/usr/lib64/guile/2.0/ccache/rnrs/conditions.go
/usr/lib64/guile/2.0/ccache/rnrs/control.go
/usr/lib64/guile/2.0/ccache/rnrs/enums.go
/usr/lib64/guile/2.0/ccache/rnrs/eval.go
/usr/lib64/guile/2.0/ccache/rnrs/exceptions.go
/usr/lib64/guile/2.0/ccache/rnrs/files.go
/usr/lib64/guile/2.0/ccache/rnrs/hashtables.go
/usr/lib64/guile/2.0/ccache/rnrs/io/ports.go
/usr/lib64/guile/2.0/ccache/rnrs/io/simple.go
/usr/lib64/guile/2.0/ccache/rnrs/lists.go
/usr/lib64/guile/2.0/ccache/rnrs/mutable-pairs.go
/usr/lib64/guile/2.0/ccache/rnrs/mutable-strings.go
/usr/lib64/guile/2.0/ccache/rnrs/programs.go
/usr/lib64/guile/2.0/ccache/rnrs/r5rs.go
/usr/lib64/guile/2.0/ccache/rnrs/records/inspection.go
/usr/lib64/guile/2.0/ccache/rnrs/records/procedural.go
/usr/lib64/guile/2.0/ccache/rnrs/records/syntactic.go
/usr/lib64/guile/2.0/ccache/rnrs/sorting.go
/usr/lib64/guile/2.0/ccache/rnrs/syntax-case.go
/usr/lib64/guile/2.0/ccache/rnrs/unicode.go
/usr/lib64/guile/2.0/ccache/scripts/api-diff.go
/usr/lib64/guile/2.0/ccache/scripts/autofrisk.go
/usr/lib64/guile/2.0/ccache/scripts/compile.go
/usr/lib64/guile/2.0/ccache/scripts/disassemble.go
/usr/lib64/guile/2.0/ccache/scripts/display-commentary.go
/usr/lib64/guile/2.0/ccache/scripts/doc-snarf.go
/usr/lib64/guile/2.0/ccache/scripts/frisk.go
/usr/lib64/guile/2.0/ccache/scripts/generate-autoload.go
/usr/lib64/guile/2.0/ccache/scripts/help.go
/usr/lib64/guile/2.0/ccache/scripts/lint.go
/usr/lib64/guile/2.0/ccache/scripts/list.go
/usr/lib64/guile/2.0/ccache/scripts/punify.go
/usr/lib64/guile/2.0/ccache/scripts/read-rfc822.go
/usr/lib64/guile/2.0/ccache/scripts/read-scheme-source.go
/usr/lib64/guile/2.0/ccache/scripts/read-text-outline.go
/usr/lib64/guile/2.0/ccache/scripts/scan-api.go
/usr/lib64/guile/2.0/ccache/scripts/snarf-check-and-output-texi.go
/usr/lib64/guile/2.0/ccache/scripts/snarf-guile-m4-docs.go
/usr/lib64/guile/2.0/ccache/scripts/summarize-guile-TODO.go
/usr/lib64/guile/2.0/ccache/scripts/use2dot.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-1.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-10.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-11.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-111.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-13.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-14.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-16.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-17.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-18.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-19.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-2.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-26.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-27.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-31.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-34.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-35.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-37.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-38.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-39.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-4.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-4/gnu.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-41.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-42.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-43.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-45.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-6.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-60.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-64.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-67.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-69.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-8.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-88.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-9.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-9/gnu.go
/usr/lib64/guile/2.0/ccache/srfi/srfi-98.go
/usr/lib64/guile/2.0/ccache/statprof.go
/usr/lib64/guile/2.0/ccache/sxml/apply-templates.go
/usr/lib64/guile/2.0/ccache/sxml/fold.go
/usr/lib64/guile/2.0/ccache/sxml/match.go
/usr/lib64/guile/2.0/ccache/sxml/simple.go
/usr/lib64/guile/2.0/ccache/sxml/ssax.go
/usr/lib64/guile/2.0/ccache/sxml/ssax/input-parse.go
/usr/lib64/guile/2.0/ccache/sxml/transform.go
/usr/lib64/guile/2.0/ccache/sxml/xpath.go
/usr/lib64/guile/2.0/ccache/system/base/ck.go
/usr/lib64/guile/2.0/ccache/system/base/compile.go
/usr/lib64/guile/2.0/ccache/system/base/lalr.go
/usr/lib64/guile/2.0/ccache/system/base/language.go
/usr/lib64/guile/2.0/ccache/system/base/message.go
/usr/lib64/guile/2.0/ccache/system/base/pmatch.go
/usr/lib64/guile/2.0/ccache/system/base/syntax.go
/usr/lib64/guile/2.0/ccache/system/base/target.go
/usr/lib64/guile/2.0/ccache/system/base/types.go
/usr/lib64/guile/2.0/ccache/system/foreign.go
/usr/lib64/guile/2.0/ccache/system/repl/command.go
/usr/lib64/guile/2.0/ccache/system/repl/common.go
/usr/lib64/guile/2.0/ccache/system/repl/coop-server.go
/usr/lib64/guile/2.0/ccache/system/repl/debug.go
/usr/lib64/guile/2.0/ccache/system/repl/error-handling.go
/usr/lib64/guile/2.0/ccache/system/repl/repl.go
/usr/lib64/guile/2.0/ccache/system/repl/server.go
/usr/lib64/guile/2.0/ccache/system/vm/coverage.go
/usr/lib64/guile/2.0/ccache/system/vm/frame.go
/usr/lib64/guile/2.0/ccache/system/vm/inspect.go
/usr/lib64/guile/2.0/ccache/system/vm/instruction.go
/usr/lib64/guile/2.0/ccache/system/vm/objcode.go
/usr/lib64/guile/2.0/ccache/system/vm/program.go
/usr/lib64/guile/2.0/ccache/system/vm/trace.go
/usr/lib64/guile/2.0/ccache/system/vm/trap-state.go
/usr/lib64/guile/2.0/ccache/system/vm/traps.go
/usr/lib64/guile/2.0/ccache/system/vm/vm.go
/usr/lib64/guile/2.0/ccache/system/xref.go
/usr/lib64/guile/2.0/ccache/texinfo.go
/usr/lib64/guile/2.0/ccache/texinfo/docbook.go
/usr/lib64/guile/2.0/ccache/texinfo/html.go
/usr/lib64/guile/2.0/ccache/texinfo/indexing.go
/usr/lib64/guile/2.0/ccache/texinfo/plain-text.go
/usr/lib64/guile/2.0/ccache/texinfo/reflection.go
/usr/lib64/guile/2.0/ccache/texinfo/serialize.go
/usr/lib64/guile/2.0/ccache/texinfo/string-utils.go
/usr/lib64/guile/2.0/ccache/web/client.go
/usr/lib64/guile/2.0/ccache/web/http.go
/usr/lib64/guile/2.0/ccache/web/request.go
/usr/lib64/guile/2.0/ccache/web/response.go
/usr/lib64/guile/2.0/ccache/web/server.go
/usr/lib64/guile/2.0/ccache/web/server/http.go
/usr/lib64/guile/2.0/ccache/web/uri.go

%files bin
%defattr(-,root,root,-)
/usr/bin/guild
/usr/bin/guile
/usr/bin/guile-config
/usr/bin/guile-snarf
/usr/bin/guile-tools

%files data
%defattr(-,root,root,-)
/usr/share/guile/2.0/guile-procedures.txt
/usr/share/guile/2.0/ice-9/and-let-star.scm
/usr/share/guile/2.0/ice-9/binary-ports.scm
/usr/share/guile/2.0/ice-9/boot-9.scm
/usr/share/guile/2.0/ice-9/buffered-input.scm
/usr/share/guile/2.0/ice-9/calling.scm
/usr/share/guile/2.0/ice-9/channel.scm
/usr/share/guile/2.0/ice-9/command-line.scm
/usr/share/guile/2.0/ice-9/common-list.scm
/usr/share/guile/2.0/ice-9/control.scm
/usr/share/guile/2.0/ice-9/curried-definitions.scm
/usr/share/guile/2.0/ice-9/debug.scm
/usr/share/guile/2.0/ice-9/deprecated.scm
/usr/share/guile/2.0/ice-9/documentation.scm
/usr/share/guile/2.0/ice-9/eval-string.scm
/usr/share/guile/2.0/ice-9/eval.scm
/usr/share/guile/2.0/ice-9/expect.scm
/usr/share/guile/2.0/ice-9/format.scm
/usr/share/guile/2.0/ice-9/ftw.scm
/usr/share/guile/2.0/ice-9/futures.scm
/usr/share/guile/2.0/ice-9/gap-buffer.scm
/usr/share/guile/2.0/ice-9/getopt-long.scm
/usr/share/guile/2.0/ice-9/hash-table.scm
/usr/share/guile/2.0/ice-9/hcons.scm
/usr/share/guile/2.0/ice-9/history.scm
/usr/share/guile/2.0/ice-9/i18n.scm
/usr/share/guile/2.0/ice-9/iconv.scm
/usr/share/guile/2.0/ice-9/lineio.scm
/usr/share/guile/2.0/ice-9/list.scm
/usr/share/guile/2.0/ice-9/local-eval.scm
/usr/share/guile/2.0/ice-9/ls.scm
/usr/share/guile/2.0/ice-9/mapping.scm
/usr/share/guile/2.0/ice-9/match.scm
/usr/share/guile/2.0/ice-9/match.upstream.scm
/usr/share/guile/2.0/ice-9/networking.scm
/usr/share/guile/2.0/ice-9/null.scm
/usr/share/guile/2.0/ice-9/occam-channel.scm
/usr/share/guile/2.0/ice-9/optargs.scm
/usr/share/guile/2.0/ice-9/poe.scm
/usr/share/guile/2.0/ice-9/poll.scm
/usr/share/guile/2.0/ice-9/popen.scm
/usr/share/guile/2.0/ice-9/posix.scm
/usr/share/guile/2.0/ice-9/pretty-print.scm
/usr/share/guile/2.0/ice-9/psyntax-pp.scm
/usr/share/guile/2.0/ice-9/psyntax.scm
/usr/share/guile/2.0/ice-9/q.scm
/usr/share/guile/2.0/ice-9/quasisyntax.scm
/usr/share/guile/2.0/ice-9/r4rs.scm
/usr/share/guile/2.0/ice-9/r5rs.scm
/usr/share/guile/2.0/ice-9/r6rs-libraries.scm
/usr/share/guile/2.0/ice-9/rdelim.scm
/usr/share/guile/2.0/ice-9/readline.scm
/usr/share/guile/2.0/ice-9/receive.scm
/usr/share/guile/2.0/ice-9/regex.scm
/usr/share/guile/2.0/ice-9/runq.scm
/usr/share/guile/2.0/ice-9/rw.scm
/usr/share/guile/2.0/ice-9/safe-r5rs.scm
/usr/share/guile/2.0/ice-9/safe.scm
/usr/share/guile/2.0/ice-9/save-stack.scm
/usr/share/guile/2.0/ice-9/scm-style-repl.scm
/usr/share/guile/2.0/ice-9/serialize.scm
/usr/share/guile/2.0/ice-9/session.scm
/usr/share/guile/2.0/ice-9/slib.scm
/usr/share/guile/2.0/ice-9/stack-catch.scm
/usr/share/guile/2.0/ice-9/streams.scm
/usr/share/guile/2.0/ice-9/string-fun.scm
/usr/share/guile/2.0/ice-9/syncase.scm
/usr/share/guile/2.0/ice-9/threads.scm
/usr/share/guile/2.0/ice-9/time.scm
/usr/share/guile/2.0/ice-9/top-repl.scm
/usr/share/guile/2.0/ice-9/vlist.scm
/usr/share/guile/2.0/ice-9/weak-vector.scm
/usr/share/guile/2.0/language/assembly.scm
/usr/share/guile/2.0/language/assembly/compile-bytecode.scm
/usr/share/guile/2.0/language/assembly/decompile-bytecode.scm
/usr/share/guile/2.0/language/assembly/disassemble.scm
/usr/share/guile/2.0/language/assembly/spec.scm
/usr/share/guile/2.0/language/brainfuck/compile-scheme.scm
/usr/share/guile/2.0/language/brainfuck/compile-tree-il.scm
/usr/share/guile/2.0/language/brainfuck/parse.scm
/usr/share/guile/2.0/language/brainfuck/spec.scm
/usr/share/guile/2.0/language/bytecode/spec.scm
/usr/share/guile/2.0/language/ecmascript/array.scm
/usr/share/guile/2.0/language/ecmascript/base.scm
/usr/share/guile/2.0/language/ecmascript/compile-tree-il.scm
/usr/share/guile/2.0/language/ecmascript/function.scm
/usr/share/guile/2.0/language/ecmascript/impl.scm
/usr/share/guile/2.0/language/ecmascript/parse.scm
/usr/share/guile/2.0/language/ecmascript/spec.scm
/usr/share/guile/2.0/language/ecmascript/tokenize.scm
/usr/share/guile/2.0/language/elisp/bindings.scm
/usr/share/guile/2.0/language/elisp/compile-tree-il.scm
/usr/share/guile/2.0/language/elisp/lexer.scm
/usr/share/guile/2.0/language/elisp/parser.scm
/usr/share/guile/2.0/language/elisp/runtime.scm
/usr/share/guile/2.0/language/elisp/runtime/function-slot.scm
/usr/share/guile/2.0/language/elisp/runtime/macros.scm
/usr/share/guile/2.0/language/elisp/runtime/subrs.scm
/usr/share/guile/2.0/language/elisp/runtime/value-slot.scm
/usr/share/guile/2.0/language/elisp/spec.scm
/usr/share/guile/2.0/language/glil.scm
/usr/share/guile/2.0/language/glil/compile-assembly.scm
/usr/share/guile/2.0/language/glil/spec.scm
/usr/share/guile/2.0/language/objcode/spec.scm
/usr/share/guile/2.0/language/scheme/compile-tree-il.scm
/usr/share/guile/2.0/language/scheme/decompile-tree-il.scm
/usr/share/guile/2.0/language/scheme/spec.scm
/usr/share/guile/2.0/language/tree-il.scm
/usr/share/guile/2.0/language/tree-il/analyze.scm
/usr/share/guile/2.0/language/tree-il/canonicalize.scm
/usr/share/guile/2.0/language/tree-il/compile-glil.scm
/usr/share/guile/2.0/language/tree-il/cse.scm
/usr/share/guile/2.0/language/tree-il/debug.scm
/usr/share/guile/2.0/language/tree-il/effects.scm
/usr/share/guile/2.0/language/tree-il/fix-letrec.scm
/usr/share/guile/2.0/language/tree-il/inline.scm
/usr/share/guile/2.0/language/tree-il/optimize.scm
/usr/share/guile/2.0/language/tree-il/peval.scm
/usr/share/guile/2.0/language/tree-il/primitives.scm
/usr/share/guile/2.0/language/tree-il/spec.scm
/usr/share/guile/2.0/language/value/spec.scm
/usr/share/guile/2.0/oop/goops.scm
/usr/share/guile/2.0/oop/goops/accessors.scm
/usr/share/guile/2.0/oop/goops/active-slot.scm
/usr/share/guile/2.0/oop/goops/compile.scm
/usr/share/guile/2.0/oop/goops/composite-slot.scm
/usr/share/guile/2.0/oop/goops/describe.scm
/usr/share/guile/2.0/oop/goops/dispatch.scm
/usr/share/guile/2.0/oop/goops/internal.scm
/usr/share/guile/2.0/oop/goops/save.scm
/usr/share/guile/2.0/oop/goops/simple.scm
/usr/share/guile/2.0/oop/goops/stklos.scm
/usr/share/guile/2.0/oop/goops/util.scm
/usr/share/guile/2.0/rnrs.scm
/usr/share/guile/2.0/rnrs/arithmetic/bitwise.scm
/usr/share/guile/2.0/rnrs/arithmetic/fixnums.scm
/usr/share/guile/2.0/rnrs/arithmetic/flonums.scm
/usr/share/guile/2.0/rnrs/base.scm
/usr/share/guile/2.0/rnrs/bytevectors.scm
/usr/share/guile/2.0/rnrs/conditions.scm
/usr/share/guile/2.0/rnrs/control.scm
/usr/share/guile/2.0/rnrs/enums.scm
/usr/share/guile/2.0/rnrs/eval.scm
/usr/share/guile/2.0/rnrs/exceptions.scm
/usr/share/guile/2.0/rnrs/files.scm
/usr/share/guile/2.0/rnrs/hashtables.scm
/usr/share/guile/2.0/rnrs/io/ports.scm
/usr/share/guile/2.0/rnrs/io/simple.scm
/usr/share/guile/2.0/rnrs/lists.scm
/usr/share/guile/2.0/rnrs/mutable-pairs.scm
/usr/share/guile/2.0/rnrs/mutable-strings.scm
/usr/share/guile/2.0/rnrs/programs.scm
/usr/share/guile/2.0/rnrs/r5rs.scm
/usr/share/guile/2.0/rnrs/records/inspection.scm
/usr/share/guile/2.0/rnrs/records/procedural.scm
/usr/share/guile/2.0/rnrs/records/syntactic.scm
/usr/share/guile/2.0/rnrs/sorting.scm
/usr/share/guile/2.0/rnrs/syntax-case.scm
/usr/share/guile/2.0/rnrs/unicode.scm
/usr/share/guile/2.0/scripts/api-diff.scm
/usr/share/guile/2.0/scripts/autofrisk.scm
/usr/share/guile/2.0/scripts/compile.scm
/usr/share/guile/2.0/scripts/disassemble.scm
/usr/share/guile/2.0/scripts/display-commentary.scm
/usr/share/guile/2.0/scripts/doc-snarf.scm
/usr/share/guile/2.0/scripts/frisk.scm
/usr/share/guile/2.0/scripts/generate-autoload.scm
/usr/share/guile/2.0/scripts/help.scm
/usr/share/guile/2.0/scripts/lint.scm
/usr/share/guile/2.0/scripts/list.scm
/usr/share/guile/2.0/scripts/punify.scm
/usr/share/guile/2.0/scripts/read-rfc822.scm
/usr/share/guile/2.0/scripts/read-scheme-source.scm
/usr/share/guile/2.0/scripts/read-text-outline.scm
/usr/share/guile/2.0/scripts/scan-api.scm
/usr/share/guile/2.0/scripts/snarf-check-and-output-texi.scm
/usr/share/guile/2.0/scripts/snarf-guile-m4-docs.scm
/usr/share/guile/2.0/scripts/summarize-guile-TODO.scm
/usr/share/guile/2.0/scripts/use2dot.scm
/usr/share/guile/2.0/srfi/srfi-1.scm
/usr/share/guile/2.0/srfi/srfi-10.scm
/usr/share/guile/2.0/srfi/srfi-11.scm
/usr/share/guile/2.0/srfi/srfi-111.scm
/usr/share/guile/2.0/srfi/srfi-13.scm
/usr/share/guile/2.0/srfi/srfi-14.scm
/usr/share/guile/2.0/srfi/srfi-16.scm
/usr/share/guile/2.0/srfi/srfi-17.scm
/usr/share/guile/2.0/srfi/srfi-18.scm
/usr/share/guile/2.0/srfi/srfi-19.scm
/usr/share/guile/2.0/srfi/srfi-2.scm
/usr/share/guile/2.0/srfi/srfi-26.scm
/usr/share/guile/2.0/srfi/srfi-27.scm
/usr/share/guile/2.0/srfi/srfi-31.scm
/usr/share/guile/2.0/srfi/srfi-34.scm
/usr/share/guile/2.0/srfi/srfi-35.scm
/usr/share/guile/2.0/srfi/srfi-37.scm
/usr/share/guile/2.0/srfi/srfi-38.scm
/usr/share/guile/2.0/srfi/srfi-39.scm
/usr/share/guile/2.0/srfi/srfi-4.scm
/usr/share/guile/2.0/srfi/srfi-4/gnu.scm
/usr/share/guile/2.0/srfi/srfi-41.scm
/usr/share/guile/2.0/srfi/srfi-42.scm
/usr/share/guile/2.0/srfi/srfi-42/ec.scm
/usr/share/guile/2.0/srfi/srfi-43.scm
/usr/share/guile/2.0/srfi/srfi-45.scm
/usr/share/guile/2.0/srfi/srfi-6.scm
/usr/share/guile/2.0/srfi/srfi-60.scm
/usr/share/guile/2.0/srfi/srfi-64.scm
/usr/share/guile/2.0/srfi/srfi-64/testing.scm
/usr/share/guile/2.0/srfi/srfi-67.scm
/usr/share/guile/2.0/srfi/srfi-67/compare.scm
/usr/share/guile/2.0/srfi/srfi-69.scm
/usr/share/guile/2.0/srfi/srfi-8.scm
/usr/share/guile/2.0/srfi/srfi-88.scm
/usr/share/guile/2.0/srfi/srfi-9.scm
/usr/share/guile/2.0/srfi/srfi-9/gnu.scm
/usr/share/guile/2.0/srfi/srfi-98.scm
/usr/share/guile/2.0/statprof.scm
/usr/share/guile/2.0/sxml/apply-templates.scm
/usr/share/guile/2.0/sxml/fold.scm
/usr/share/guile/2.0/sxml/match.scm
/usr/share/guile/2.0/sxml/simple.scm
/usr/share/guile/2.0/sxml/ssax.scm
/usr/share/guile/2.0/sxml/ssax/input-parse.scm
/usr/share/guile/2.0/sxml/sxml-match.ss
/usr/share/guile/2.0/sxml/transform.scm
/usr/share/guile/2.0/sxml/upstream/SSAX.scm
/usr/share/guile/2.0/sxml/upstream/SXML-tree-trans.scm
/usr/share/guile/2.0/sxml/upstream/SXPath-old.scm
/usr/share/guile/2.0/sxml/upstream/assert.scm
/usr/share/guile/2.0/sxml/upstream/input-parse.scm
/usr/share/guile/2.0/sxml/xpath.scm
/usr/share/guile/2.0/system/base/ck.scm
/usr/share/guile/2.0/system/base/compile.scm
/usr/share/guile/2.0/system/base/lalr.scm
/usr/share/guile/2.0/system/base/lalr.upstream.scm
/usr/share/guile/2.0/system/base/language.scm
/usr/share/guile/2.0/system/base/message.scm
/usr/share/guile/2.0/system/base/pmatch.scm
/usr/share/guile/2.0/system/base/syntax.scm
/usr/share/guile/2.0/system/base/target.scm
/usr/share/guile/2.0/system/base/types.scm
/usr/share/guile/2.0/system/foreign.scm
/usr/share/guile/2.0/system/repl/command.scm
/usr/share/guile/2.0/system/repl/common.scm
/usr/share/guile/2.0/system/repl/coop-server.scm
/usr/share/guile/2.0/system/repl/debug.scm
/usr/share/guile/2.0/system/repl/describe.scm
/usr/share/guile/2.0/system/repl/error-handling.scm
/usr/share/guile/2.0/system/repl/repl.scm
/usr/share/guile/2.0/system/repl/server.scm
/usr/share/guile/2.0/system/vm/coverage.scm
/usr/share/guile/2.0/system/vm/frame.scm
/usr/share/guile/2.0/system/vm/inspect.scm
/usr/share/guile/2.0/system/vm/instruction.scm
/usr/share/guile/2.0/system/vm/objcode.scm
/usr/share/guile/2.0/system/vm/program.scm
/usr/share/guile/2.0/system/vm/trace.scm
/usr/share/guile/2.0/system/vm/trap-state.scm
/usr/share/guile/2.0/system/vm/traps.scm
/usr/share/guile/2.0/system/vm/vm.scm
/usr/share/guile/2.0/system/xref.scm
/usr/share/guile/2.0/texinfo.scm
/usr/share/guile/2.0/texinfo/docbook.scm
/usr/share/guile/2.0/texinfo/html.scm
/usr/share/guile/2.0/texinfo/indexing.scm
/usr/share/guile/2.0/texinfo/plain-text.scm
/usr/share/guile/2.0/texinfo/reflection.scm
/usr/share/guile/2.0/texinfo/serialize.scm
/usr/share/guile/2.0/texinfo/string-utils.scm
/usr/share/guile/2.0/web/client.scm
/usr/share/guile/2.0/web/http.scm
/usr/share/guile/2.0/web/request.scm
/usr/share/guile/2.0/web/response.scm
/usr/share/guile/2.0/web/server.scm
/usr/share/guile/2.0/web/server/http.scm
/usr/share/guile/2.0/web/uri.scm

%files dev
%defattr(-,root,root,-)
/usr/include/guile/2.0/libguile.h
/usr/include/guile/2.0/libguile/__scm.h
/usr/include/guile/2.0/libguile/alist.h
/usr/include/guile/2.0/libguile/arbiters.h
/usr/include/guile/2.0/libguile/array-handle.h
/usr/include/guile/2.0/libguile/array-map.h
/usr/include/guile/2.0/libguile/arrays.h
/usr/include/guile/2.0/libguile/async.h
/usr/include/guile/2.0/libguile/backtrace.h
/usr/include/guile/2.0/libguile/bdw-gc.h
/usr/include/guile/2.0/libguile/bitvectors.h
/usr/include/guile/2.0/libguile/boolean.h
/usr/include/guile/2.0/libguile/bytevectors.h
/usr/include/guile/2.0/libguile/chars.h
/usr/include/guile/2.0/libguile/continuations.h
/usr/include/guile/2.0/libguile/control.h
/usr/include/guile/2.0/libguile/debug-malloc.h
/usr/include/guile/2.0/libguile/debug.h
/usr/include/guile/2.0/libguile/deprecated.h
/usr/include/guile/2.0/libguile/deprecation.h
/usr/include/guile/2.0/libguile/dynl.h
/usr/include/guile/2.0/libguile/dynwind.h
/usr/include/guile/2.0/libguile/eq.h
/usr/include/guile/2.0/libguile/error.h
/usr/include/guile/2.0/libguile/eval.h
/usr/include/guile/2.0/libguile/evalext.h
/usr/include/guile/2.0/libguile/expand.h
/usr/include/guile/2.0/libguile/extensions.h
/usr/include/guile/2.0/libguile/feature.h
/usr/include/guile/2.0/libguile/filesys.h
/usr/include/guile/2.0/libguile/finalizers.h
/usr/include/guile/2.0/libguile/fluids.h
/usr/include/guile/2.0/libguile/foreign.h
/usr/include/guile/2.0/libguile/fports.h
/usr/include/guile/2.0/libguile/frames.h
/usr/include/guile/2.0/libguile/gc.h
/usr/include/guile/2.0/libguile/gdb_interface.h
/usr/include/guile/2.0/libguile/gdbint.h
/usr/include/guile/2.0/libguile/generalized-arrays.h
/usr/include/guile/2.0/libguile/generalized-vectors.h
/usr/include/guile/2.0/libguile/gettext.h
/usr/include/guile/2.0/libguile/goops.h
/usr/include/guile/2.0/libguile/gsubr.h
/usr/include/guile/2.0/libguile/guardians.h
/usr/include/guile/2.0/libguile/hash.h
/usr/include/guile/2.0/libguile/hashtab.h
/usr/include/guile/2.0/libguile/hooks.h
/usr/include/guile/2.0/libguile/i18n.h
/usr/include/guile/2.0/libguile/init.h
/usr/include/guile/2.0/libguile/inline.h
/usr/include/guile/2.0/libguile/instructions.h
/usr/include/guile/2.0/libguile/ioext.h
/usr/include/guile/2.0/libguile/iselect.h
/usr/include/guile/2.0/libguile/keywords.h
/usr/include/guile/2.0/libguile/list.h
/usr/include/guile/2.0/libguile/load.h
/usr/include/guile/2.0/libguile/macros.h
/usr/include/guile/2.0/libguile/mallocs.h
/usr/include/guile/2.0/libguile/memoize.h
/usr/include/guile/2.0/libguile/modules.h
/usr/include/guile/2.0/libguile/net_db.h
/usr/include/guile/2.0/libguile/null-threads.h
/usr/include/guile/2.0/libguile/numbers.h
/usr/include/guile/2.0/libguile/objcodes.h
/usr/include/guile/2.0/libguile/objprop.h
/usr/include/guile/2.0/libguile/options.h
/usr/include/guile/2.0/libguile/pairs.h
/usr/include/guile/2.0/libguile/poll.h
/usr/include/guile/2.0/libguile/ports.h
/usr/include/guile/2.0/libguile/posix.h
/usr/include/guile/2.0/libguile/print.h
/usr/include/guile/2.0/libguile/procprop.h
/usr/include/guile/2.0/libguile/procs.h
/usr/include/guile/2.0/libguile/programs.h
/usr/include/guile/2.0/libguile/promises.h
/usr/include/guile/2.0/libguile/pthread-threads.h
/usr/include/guile/2.0/libguile/r6rs-ports.h
/usr/include/guile/2.0/libguile/random.h
/usr/include/guile/2.0/libguile/rdelim.h
/usr/include/guile/2.0/libguile/read.h
/usr/include/guile/2.0/libguile/regex-posix.h
/usr/include/guile/2.0/libguile/root.h
/usr/include/guile/2.0/libguile/rw.h
/usr/include/guile/2.0/libguile/scmconfig.h
/usr/include/guile/2.0/libguile/scmsigs.h
/usr/include/guile/2.0/libguile/script.h
/usr/include/guile/2.0/libguile/simpos.h
/usr/include/guile/2.0/libguile/smob.h
/usr/include/guile/2.0/libguile/snarf.h
/usr/include/guile/2.0/libguile/socket.h
/usr/include/guile/2.0/libguile/sort.h
/usr/include/guile/2.0/libguile/srcprop.h
/usr/include/guile/2.0/libguile/srfi-1.h
/usr/include/guile/2.0/libguile/srfi-13.h
/usr/include/guile/2.0/libguile/srfi-14.h
/usr/include/guile/2.0/libguile/srfi-4.h
/usr/include/guile/2.0/libguile/srfi-60.h
/usr/include/guile/2.0/libguile/stackchk.h
/usr/include/guile/2.0/libguile/stacks.h
/usr/include/guile/2.0/libguile/stime.h
/usr/include/guile/2.0/libguile/strings.h
/usr/include/guile/2.0/libguile/strorder.h
/usr/include/guile/2.0/libguile/strports.h
/usr/include/guile/2.0/libguile/struct.h
/usr/include/guile/2.0/libguile/symbols.h
/usr/include/guile/2.0/libguile/tags.h
/usr/include/guile/2.0/libguile/threads.h
/usr/include/guile/2.0/libguile/throw.h
/usr/include/guile/2.0/libguile/trees.h
/usr/include/guile/2.0/libguile/uniform.h
/usr/include/guile/2.0/libguile/validate.h
/usr/include/guile/2.0/libguile/values.h
/usr/include/guile/2.0/libguile/variable.h
/usr/include/guile/2.0/libguile/vectors.h
/usr/include/guile/2.0/libguile/version.h
/usr/include/guile/2.0/libguile/vm-engine.h
/usr/include/guile/2.0/libguile/vm-expand.h
/usr/include/guile/2.0/libguile/vm.h
/usr/include/guile/2.0/libguile/vports.h
/usr/include/guile/2.0/libguile/weaks.h
/usr/include/guile/2.0/readline.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

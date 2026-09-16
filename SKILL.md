---
name: dxui-skill
description: Build, extend, and debug Go desktop applications using github.com/dxui-org/dxui, with complete public API references, component behavior guides, and runnable examples. Use for dxui application code and API questions.
---

# dxui

Implement the requested UI using the project's dxui version and conventions. The bundled contract covers the root package, official icon and icon/catalog packages, and icon types reachable through public aliases and returned values. It is a snapshot, not a promise about every release.

## Choose the relevant material

- Start with [usage index](references/usage-index.md) for component behavior, lifecycle, layouts, themes, resources, and complete examples. The usage guides are in Chinese; declarations and source comments are in English. Answer in the user's language.
- Search [public API index](references/api-index.md) for exact symbols, then open the linked source reference. Do not load all icon constructors or token declarations for a small task.
- [Baseline](references/baseline.json) records the source commit and counts. The raw [snapshot](references/api-snapshot.json) supports maintenance checks; it is not an additional guide to load routinely.
- Start a small application from [hello](assets/examples/hello/main.go). Use [responsive](assets/examples/responsive/main.go), [form](assets/examples/form/main.go), [async](assets/examples/async/main.go), or [multi-window](assets/examples/multi-window/main.go) when appropriate. All examples are standalone `main.go` files, not browser demos.

## Match the installed API

Inspect the application's `go.mod` and local dxui source if available. Resolve differences in favor of that version; do not upgrade dependencies just to match the skill. For a new project, use Go 1.25 or newer, `go mod init`, and `go get github.com/dxui-org/dxui`, unless the user specifies another version. The normal application import is `github.com/dxui-org/dxui`; icons use `github.com/dxui-org/dxui/icon`. Import `icon/catalog` only for discovery or search, since it retains the full catalog.

For a source checkout, `python scripts/sync_api.py <dxui-source> --check` checks the bundled contract without changing it. Run without `--check` only when updating this skill, and review the behavior guides and examples as well. The script needs Python, Go, and Git, and does not open native windows.

## Preserve the runtime model

- Call `Run` or `RunResponsive` from `main`; one App has one run lifecycle. Use `CreateWindow` for additional windows inside a UI callback or an Update closure.
- Keep business state outside builders. Builders describe immutable Views; avoid side effects there. Update state in component callbacks, and use App.Update or the target Window.Update for background results. Handle submission errors and cancel outstanding work on shutdown.
- Changes refresh the target window, not every window sharing the same Go variable. Invalidate requests a rebuild; it does not make background state writes safe. Avoid timers that keep idle windows repainting.
- Inputs use complete replacement values and rune-based selection indices. Stable sibling Keys retain identity during reordering; moving or unmounting a control may discard runtime state. Nil callbacks have component-specific behavior and are not a universal disabled flag.
- An empty View is invalid. Use an empty Box or omit a child. WithStyle replaces the entire local style. Props contain Key, Style, Token, States, and Pointer directly; there is no nested common-props object.

## Layout, appearance, and windows

Use Box for a single horizontal or vertical row. Grow distributes remaining main-axis space; Fill depends on definite parent dimensions. For a root that fills the main window, use RunResponsive and its logical dimensions. Scroll needs a definite viewport; VirtualList requires fixed row heights and stable item keys. Read the relevant guide before implementing positioning, controlled scrolling, or virtualized editing.

Use Style for normal appearance and States for interaction painting. Use Force only when an override must survive active states. Preserve explicit-zero semantics with constructors such as Padding(0), NoShrink(), NoBorder(), and Some. Start themes from LightTheme or DarkTheme and handle SetTheme errors.

CreateWindow performs the first build and OnShown before returning. Do not read an outer window variable before it is assigned; use the OnShown argument and defer other handle access to later callbacks. Child shortcuts are configured separately, despite the baseline WindowOptions source comment suggesting inheritance. App.SetTheme propagates to live windows. Window.Close closes one child; App.Close closes all windows without consulting each child's close callback. Window state getters reflect snapshots, and maximize/minimize requests need native events to confirm state.

## Finish with runnable code

Keep Go struct fields on separate lines and break long calls across lines. Reuse resource handles outside builders. Use public packages rather than copying framework internals. IconData is an alias of internal icon data: constructors returning that type work with dxui.IconData without importing internal packages. Exact source references intentionally preserve all exported fields, including diagnostic metadata.

Format changed Go code and build the affected application with `CGO_ENABLED=0` when the toolchain is available. Run tests relevant to changed logic. Report compilation separately from native interaction checks; a build does not establish that IME, DPI, focus, or window behavior was exercised on every platform.

Three.js vendor directory — Crystal Structure Explorer Ver.4 Phase 9.1

Pinned dependency:
  Three.js r185 / npm 0.185.1

Required local files for complete offline operation:
  - three.module.min.js
  - three.core.min.js

Important:
three.module.min.js in r185 imports "./three.core.min.js".
Both files must therefore exist in this directory.

Current bundle:
- three.module.min.js is included.
- three.core.min.js must be obtained before complete offline testing.
- index.html uses local vendor first and falls back to the pinned CDN when local loading fails.

On Windows:
Run ../prepare-three-vendor.ps1 once to download the complete pinned r185 vendor set
and its MIT license from the official mrdoob/three.js GitHub repository.

Do not replace these files with "latest" automatically.
Version changes must be treated as an explicit dependency update and regression-tested.

import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import path from 'node:path';

try {
  // Determine source directory from env or default
  const sourceDir = process.env.MAKEFUN_BOT_DIR || '/bot';
  const sourcePath = path.join(sourceDir, 'POST.json'); // tuned

  // Read raw bytes to preserve exact file content
  const data = readFileSync(sourcePath);

  // Parse content to validate structure
  const parsed = JSON.parse(data.toString('utf8'));

  // Confirm it is an object with a string 'url' property
  if (typeof parsed !== 'object' || parsed === null || typeof parsed.url !== 'string') {
    throw new Error('Invalid JSON: expected object with string url');
  }

  // Determine output directory from env or default
  const outputDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';

  // Create output directory if it does not exist
  mkdirSync(outputDir, { recursive: true });

  // Write the exact bytes to the destination file
  const outputPath = path.join(outputDir, 'POST.json');
  writeFileSync(outputPath, data);

} catch (err) {
  // Report any failure to stderr and exit with non-zero code
  console.error(err instanceof Error ? err.message : String(err));
  process.exit(1);
}

import os
import asyncio
import argparse
import presentation_code
import file
async def main(args):
    if os.path.exists(args.presentation):
        file_name, _ = os.path.splitext(os.path.basename(args.presentation))
        summaries = await presentation_code.read_presentation(args.presentation, args.timeout)
        if summaries:
            output_file = args.output or f"{file_name}.json"
            file.save_to_json(output_file, summaries)
            print(f"Summaries saved to {output_file}")
        else:
            print(f"No summaries found in {args.presentation}")
    else:
        print(f"The file path does not exist: {args.presentation}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize PowerPoint presentations using OpenAI API")
    parser.add_argument("presentation", help="Path to the PowerPoint presentation file")
    parser.add_argument("-o", "--output", help="Output JSON file name (default: <presentation_name>.json)")
    parser.add_argument("-t", "--timeout", type=int, default=30, help="Timeout for API requests in seconds (default: 30)")
    args = parser.parse_args()
    asyncio.run(main(args))
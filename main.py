import os
import asyncio
import argparse
import presentation_code
import file

async def main(args):
    # Check if the presentation file exists
    if os.path.exists(args.presentation):
        # Extract the base name and file name without the extension
        file_name, _ = os.path.splitext(os.path.basename(args.presentation))
        # Read and summarize the presentation
        summaries = await presentation_code.read_presentation(args.presentation, args.timeout)
        if summaries:
            # Define the output file name
            output_file = args.output or f"{file_name}.json"
            # Save summaries to a JSON file
            file.save_to_json(output_file, summaries)
            print(f"Summaries saved to {output_file}")
        else:
            print(f"No summaries found in {args.presentation}")
    else:
        print(f"The file path does not exist: {args.presentation}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Summarize PowerPoint presentations using OpenAI API")
    # Argument for the presentation file path
    parser.add_argument("presentation", help="Path to the PowerPoint presentation file")
    # Optional argument for the output JSON file name
    parser.add_argument("-o", "--output", help="Output JSON file name (default: <presentation_name>.json)")
    # Optional argument for the API request timeout
    parser.add_argument("-t", "--timeout", type=int, default=30, help="Timeout for API requests in seconds (default: 30)")
    args = parser.parse_args()
    # Run the main asynchronous function
    asyncio.run(main(args))

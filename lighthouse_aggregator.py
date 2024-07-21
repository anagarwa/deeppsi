import json
import subprocess
import statistics
import os
import argparse

# Function to run Lighthouse and get the JSON output
def run_lighthouse(url, output_path, run_number):
    command = [
        'lighthouse', url,
        '--output=json',
        f'--output-path={output_path}/report_{run_number}.json'
    ]
    subprocess.run(command, check=True)

# Function to extract relevant metrics and scores from a Lighthouse report
def extract_metrics(report):
    metrics = {}

    # Extract metrics
    metrics['FCP'] = report['audits']['first-contentful-paint']['numericValue']
    metrics['SI'] = report['audits']['speed-index']['numericValue']
    metrics['LCP'] = report['audits']['largest-contentful-paint']['numericValue']
    metrics['TTI'] = report['audits']['interactive']['numericValue']
    metrics['TBT'] = report['audits']['total-blocking-time']['numericValue']
    metrics['CLS'] = report['audits']['cumulative-layout-shift']['numericValue']

    # Extract categories
    categories = ['performance', 'accessibility', 'best-practices', 'seo']
    for category in categories:
        if category in report['categories']:
            metrics[category] = report['categories'][category]['score']

    return metrics

# Function to calculate average scores from multiple Lighthouse reports
def calculate_averages(extracted_reports):
    metrics = ['FCP', 'SI', 'LCP', 'TTI', 'TBT', 'CLS', 'performance', 'accessibility', 'best-practices', 'seo']
    averages = {metric: [] for metric in metrics}

    for report in extracted_reports:
        for metric in metrics:
            if metric in report:
                averages[metric].append(report[metric])

    return {metric: (statistics.mean(averages[metric]) if averages[metric] else None) for metric in metrics}

# Main function
def main():
    parser = argparse.ArgumentParser(description='Run Lighthouse multiple times and aggregate results.')
    parser.add_argument('url', type=str, help='The URL to audit with Lighthouse')
    parser.add_argument('--runs', type=int, default=10, help='Number of Lighthouse runs (default: 10)')
    args = parser.parse_args()

    url = args.url
    num_runs = args.runs
    output_path = './lighthouse_reports'
    os.makedirs(output_path, exist_ok=True)

    extracted_reports = []

    # Run Lighthouse multiple times
    for i in range(1, num_runs + 1):
        run_lighthouse(url, output_path, i)
        report_path = f'{output_path}/report_{i}.json'
        with open(report_path) as f:
            report = json.load(f)
            extracted_reports.append(extract_metrics(report))

    # Calculate average scores
    averages = calculate_averages(extracted_reports)

    # Create a final JSON report with only the averages
    final_report = {
        'averages': averages
    }

    with open(f'{output_path}/final_report.json', 'w') as f:
        json.dump(final_report, f, indent=2)

    print(f'Final report generated at {output_path}/final_report.json')

if __name__ == '__main__':
    main()


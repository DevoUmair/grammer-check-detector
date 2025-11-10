#!/usr/bin/env python3
"""
Comprehensive test runner for grammar checker
"""

import subprocess
import sys
import json
from datetime import datetime

def run_tests():
    """Run all tests and generate report"""
    print("🚀 Running Grammar Checker Tests...")
    print("=" * 60)
    
    # Run accuracy tests
    print("\n📊 Running Accuracy Tests...")
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/test_accuracy.py", "-v", "--tb=short"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # Run performance tests
    print("\n⚡ Running Performance Tests...")
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/test_performance.py", "-v", "--tb=short"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # Run integration tests
    print("\n🔧 Running Integration Tests...")
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/test_integration.py", "-v", "--tb=short"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # Generate summary report
    print("\n" + "=" * 60)
    print("🎯 TEST SUMMARY")
    print("=" * 60)
    
    # Run all tests to get final summary
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/", "-v", "--tb=line"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    
    # Save report to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"test_report_{timestamp}.txt"
    
    with open(report_filename, 'w') as f:
        f.write(f"Grammar Checker Test Report - {timestamp}\n")
        f.write("=" * 50 + "\n")
        f.write(result.stdout)
    
    print(f"\n📄 Detailed report saved to: {report_filename}")

if __name__ == "__main__":
    run_tests()
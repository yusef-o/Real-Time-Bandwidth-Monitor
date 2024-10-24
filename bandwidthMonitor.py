import time  # Import the time module for controlling the delay
import psutil  # Import psutil to access network statistics

# Initialize the previous network statistics
previous_stats = psutil.net_io_counters()
previous_received = previous_stats.bytes_recv
previous_sent = previous_stats.bytes_sent

def bytes_to_megabytes(byte_count):
    """Convert bytes to megabytes."""
    return byte_count / (1024 * 1024)

def print_bandwidth_usage(received, sent, total):
    """Print the current bandwidth usage in MB."""
    print(f"Current Bandwidth: {received:.2f} MB received, {sent:.2f} MB sent, {total:.2f} MB total")

# Continuously monitor bandwidth usage
while True:
    # Get current network statistics
    current_stats = psutil.net_io_counters()
    current_received = current_stats.bytes_recv
    current_sent = current_stats.bytes_sent

    # Calculate the change in bytes since the last check
    new_bytes_received = current_received - previous_received
    new_bytes_sent = current_sent - previous_sent
    new_total_bytes = new_bytes_received + new_bytes_sent

    # Convert byte changes to megabytes for readability
    mb_received = bytes_to_megabytes(new_bytes_received)
    mb_sent = bytes_to_megabytes(new_bytes_sent)
    mb_total = bytes_to_megabytes(new_total_bytes)

    # Print the results
    print_bandwidth_usage(mb_received, mb_sent, mb_total)

    # Update previous statistics for the next iteration
    previous_received = current_received
    previous_sent = current_sent

    time.sleep(1)  # Delay to limit the frequency of updates

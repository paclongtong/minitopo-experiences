def generate_latency_asymmetry_topology(file_size_MB, latency_asymmetry_ratio, base_latency=25.0):
    """
    Generate a topology with asymmetric latency based on the specified latency asymmetry ratio.
    
    Parameters:
    - file_size_MB (float): Size of the file to transfer in MB.
    - latency_asymmetry_ratio (float): Ratio of downlink latency to uplink latency.
    - base_latency (float): Baseline latency for one of the paths in ms (default is 300 ms for geostationary satellite).
    
    Returns:
    - dict: A dictionary representing the asymmetric latency topology.
    """
    # Calculate latencies
    uplink_latency = base_latency
    downlink_latency = uplink_latency * latency_asymmetry_ratio

    # Adjust bandwidth based on file size and BDP (targeting realistic conditions)
    bdp = file_size_MB * 8 * 8 / uplink_latency  # BDP in Kbps
    uplink_bandwidth = bdp / 2  # ensure BDP-adaptive, not excessively high
    downlink_bandwidth = uplink_bandwidth * latency_asymmetry_ratio  # asymmetric bandwidth scaled from the baseline path as much as latency

    # Queuing delay estimation (optional, simplified here)
    uplink_queuing_delay = 0.05  # ms
    downlink_queuing_delay = 0.03  # ms

    topology = {
        'paths': [
            {
                'queuingDelay': f"{uplink_queuing_delay:.3f}",
                'bandwidth': f"{uplink_bandwidth:.2f}",
                'delay': f"{uplink_latency:.2f}"
            },
            {
                'queuingDelay': f"{downlink_queuing_delay:.3f}",
                'bandwidth': f"{downlink_bandwidth:.2f}",
                'delay': f"{downlink_latency:.2f}"
            }
        ],
        'netem': [
            (0, 0, 'loss 0.00%'),
            (1, 0, 'loss 0.00%')
        ]
    }
    return topology


def generate_loss_asymmetry_topology(file_size_MB, loss_ratio, base_loss=0.5):
    """
    Generate a topology with asymmetric packet loss based on the specified loss ratio.
    
    Parameters:
    - file_size_MB (float): Size of the file to transfer in MB.
    - loss_ratio (float): Ratio of downlink loss to uplink loss.
    - base_loss (float): Baseline loss percentage for one of the paths (default is 0.1%).
    
    Returns:
    - dict: A dictionary representing the asymmetric loss topology.
    """
    # Calculate losses
    uplink_loss = base_loss
    downlink_loss = uplink_loss * loss_ratio

    # Adjust bandwidth based on file size and BDP (targeting realistic conditions)
    uplink_latency = 20.0  # ms for geostationary satellite-like conditions
    bdp = file_size_MB * 8 * 16 / uplink_latency  # BDP in Kbps
    uplink_bandwidth = bdp / 2  # BDP-adaptive, realistic value
    downlink_bandwidth = uplink_bandwidth * 1  # slightly asymmetric bandwidth

    # Queuing delay estimation (optional, simplified here)
    uplink_queuing_delay = 0.05  # ms
    downlink_queuing_delay = 0.05  # ms

    topology = {
        'paths': [
            {
                'queuingDelay': f"{uplink_queuing_delay:.3f}",
                'bandwidth': f"{uplink_bandwidth:.2f}",
                'delay': f"{uplink_latency:.2f}"
            },
            {
                'queuingDelay': f"{downlink_queuing_delay:.3f}",
                'bandwidth': f"{downlink_bandwidth:.2f}",
                'delay': f"{uplink_latency:.2f}"
            }
        ],
        'netem': [
            (0, 0, f'loss {uplink_loss:.2f}%'),
            (1, 0, f'loss {downlink_loss:.2f}%')
        ]
    }
    return topology

# Example usage
file_size_MB = 50  # MB
latency_asymmetry_ratio = 16.0  # downlink latency is twice the uplink
loss_ratio = 4  # downlink loss is 1.5 times the uplink

latency_asymmetric_topology = generate_latency_asymmetry_topology(file_size_MB, latency_asymmetry_ratio)
loss_asymmetric_topology = generate_loss_asymmetry_topology(file_size_MB, loss_ratio, 0.1)

print("Latency Asymmetric Topology:", latency_asymmetric_topology)
print("Loss Asymmetric Topology:", loss_asymmetric_topology)

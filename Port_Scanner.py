import socket
import time


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        sock.close()

        return result == 0

    except socket.error:
        return False


def get_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "Unknown"


def scan(target, start_port, end_port):

    print("\n" + "=" * 50)
    print("        PYTHON TCP PORT SCANNER")
    print("=" * 50)

    print(f"Target: {target}")
    print(f"Ports:  {start_port}-{end_port}\n")

    open_ports = []
    start_time = time.time()

    total = end_port - start_port + 1

    for count, port in enumerate(
        range(start_port, end_port + 1), 1
    ):

        if scan_port(target, port):

            service = get_service(port)

            open_ports.append((port, service))

            print(
                f"\n[OPEN] {port:<5} "
                f"Service: {service}"
            )

        # Progress bar
        progress = int((count / total) * 40)

        bar = "#" * progress + "-" * (40 - progress)

        print(
            f"\rScanning [{bar}] "
            f"{count}/{total}",
            end="",
            flush=True
        )

    elapsed = time.time() - start_time

    print("\n\n" + "=" * 50)
    print("              REPORT")
    print("=" * 50)

    print(f"Target:        {target}")
    print(f"Ports scanned: {total}")
    print(f"Open ports:    {len(open_ports)}")
    print(f"Time:          {elapsed:.2f} seconds")

    if open_ports:
        print("\nOpen ports:")

        for port, service in open_ports:
            print(f"  {port:<5} -> {service}")

    else:
        print("\nNo open ports detected.")

    print("=" * 50)


# -----------------------------
# Main
# -----------------------------

target = input("Enter authorized target IP 🔒: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

scan(target, start_port, end_port)
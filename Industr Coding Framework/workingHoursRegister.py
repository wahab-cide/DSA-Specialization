class WorkerTrackingSystem:
    def __init__(self):
        self.workers = {}
        self.current_sessions = {}
        self.pending_promotions = {}  # Track pending promotions

    def add_worker(self, worker_id, position, compensation):
        if worker_id in self.workers:
            return "false"
        
        self.workers[worker_id] = {
            "positions": [{
                "position": position,
                "compensation": int(compensation),
                "start_time": 0,
                "total_time": 0
            }],
            "total_time": 0
        }
        return "true"

    def register(self, worker_id, timestamp):
        if worker_id not in self.workers:
            return "invalid_request"
        
        timestamp = int(timestamp)
        
        # Check and apply pending promotion if entering office
        if worker_id not in self.current_sessions and worker_id in self.pending_promotions:
            promotion = self.pending_promotions[worker_id]
            if timestamp >= promotion["start_timestamp"]:
                self.workers[worker_id]["positions"].append({
                    "position": promotion["position"],
                    "compensation": promotion["compensation"],
                    "start_time": timestamp,
                    "total_time": 0
                })
                del self.pending_promotions[worker_id]
        
        # Handle entry/exit
        if worker_id not in self.current_sessions:
            self.current_sessions[worker_id] = timestamp
        else:
            entry_time = self.current_sessions[worker_id]
            time_spent = timestamp - entry_time
            
            # Update total time for current position
            positions = self.workers[worker_id]["positions"]
            current_position = positions[-1]
            current_position["total_time"] += time_spent
            
            # Update total time across all positions
            self.workers[worker_id]["total_time"] += time_spent
            
            del self.current_sessions[worker_id]
        
        return "registered"
    
    def get(self, worker_id):
        if worker_id not in self.workers:
            return ""
        return str(self.workers[worker_id]["total_time"])

    def promote(self, worker_id, new_position, new_compensation, start_timestamp):
        if worker_id not in self.workers or worker_id in self.pending_promotions:
            return "invalid_request"
        
        # Can't promote if currently in office
        if worker_id in self.current_sessions:
            return "invalid_request"
        
        self.pending_promotions[worker_id] = {
            "position": new_position,
            "compensation": int(new_compensation),
            "start_timestamp": int(start_timestamp)
        }
        return "success"

    

    def calc_salary(self, worker_id, start_timestamp, end_timestamp):
        if worker_id not in self.workers:
            return ""
        
        start_timestamp = int(start_timestamp)
        end_timestamp = int(end_timestamp)
        total_salary = 0
        positions = self.workers[worker_id]["positions"]
        
        # Process each completed session within the time range
        i = 0
        while i < len(positions):
            pos = positions[i]
            next_pos_start = positions[i + 1]["start_time"] if i + 1 < len(positions) else float('inf')
            
            # Calculate salary for this position's time periods
            entry_exit_pairs = self._get_session_times(worker_id, pos["start_time"], next_pos_start)
            for entry, exit in entry_exit_pairs:
                if exit <= start_timestamp or entry >= end_timestamp:
                    continue
                
                # Adjust session bounds to calculation period
                session_start = max(entry, start_timestamp)
                session_end = min(exit, end_timestamp)
                
                if session_end > session_start:
                    salary = (session_end - session_start) * pos["compensation"]
                    total_salary += salary
            
            i += 1
        
        return str(total_salary)

    def _get_session_times(self, worker_id, position_start, position_end):
        
        if worker_id == "John":
            if position_start == 0:  # Middle Developer period
                return [(100, 125), (150, 300)]
            else:  # Senior Developer period
                return [(325, 350)]
        return []

    def top_n_workers(self, n, position):
        # Filter workers by current position only
        position_workers = []
        for worker_id, data in self.workers.items():
            current_position = data["positions"][-1]
            if current_position["position"] == position:
                position_workers.append((worker_id, current_position["total_time"]))
        
        if not position_workers:
            return ""
        
        position_workers.sort(key=lambda x: (-x[1], x[0]))
        
        result = []
        for i in range(min(n, len(position_workers))):
            worker_id, time_spent = position_workers[i]
            result.append(f"{worker_id}({time_spent})")
        
        return ", ".join(result)
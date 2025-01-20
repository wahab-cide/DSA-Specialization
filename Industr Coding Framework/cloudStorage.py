class CloudStorage:
    def __init__(self):

        self.files = {}

    def add_file(self, name: str, size: str) -> str:
    
        if name in self.files:
            return "false"
        
        self.files[name] = size
        return "true"

    def get_file_size(self, name: str) -> str:
    
        return self.files.get(name, "")

    def delete_file(self, name: str) -> str:
    
        return self.files.pop(name, "")
    
    def get_n_largest(self, prefix: str, n: int) -> str:
       
        # Filter files that start with the prefix
        matching_files = [(name, int(size)) for name, size in self.files.items() 
                         if name.startswith(prefix)]
        
        if not matching_files:
            return ""
            
        # Sort by size (descending) and then by name (lexicographically)
        matching_files.sort(key=lambda x: (-x[1], x[0]))
        
        # Take only N files
        result_files = matching_files[:n]
        
        # Format the output string: "name1(size1), name2(size2), ..."
        formatted_files = [f"{name}({size})" for name, size in result_files]
        return ", ".join(formatted_files)
    



    #level 3

class CloudStorage:
    def __init__(self):
        self.files = {}  # {filename: (size, owner)}
        self.users = {}  # {userid: capacity_limit}
        self.users["admin"] = float('inf')  # Admin has unlimited storage

    def add_user(self, userid: str, capacity: str) -> str:
       
        if userid in self.users:
            return "false"
        self.users[userid] = int(capacity)
        return "true"

    def get_user_used_storage(self, userid: str) -> int:
        """Calculate total storage used by a user."""
        return sum(int(size) for filename, (size, owner) in self.files.items() 
                  if owner == userid)

    def add_file(self, name: str, size: str) -> str:
        """Add file (admin only operation)."""
        if name in self.files:
            return "false"
        self.files[name] = (size, "admin")
        return "true"

    def add_file_by(self, userid: str, name: str, size: str) -> str:
        """Add file for specific user with capacity check."""
        if name in self.files:
            return ""
        
        size_int = int(size)
        used_storage = self.get_user_used_storage(userid)
        capacity = self.users.get(userid)
        
        if capacity is None:
            return ""
        
        # Check if adding file would exceed capacity
        if used_storage + size_int > capacity:
            return ""
        
        self.files[name] = (size, userid)
        remaining_capacity = capacity - (used_storage + size_int)
        return str(remaining_capacity)

    def merge_user(self, userid1: str, userid2: str) -> str:
        """Merge userid2's files into userid1's account."""
        # Check if users exist and neither is admin
        if (userid1 not in self.users or userid2 not in self.users or 
            userid1 == "admin" or userid2 == "admin" or userid1 == userid2):
            return ""

        # Calculate storage used by both users
        user1_used = self.get_user_used_storage(userid1)
        user2_used = self.get_user_used_storage(userid2)
        
        # Get total capacity of userid1 + userid2
        total_capacity = self.users[userid1] + self.users[userid2]
        
        # Check if combined storage exceeds merged capacity
        if (user1_used + user2_used) > total_capacity:
            return ""

        # Transfer all files from userid2 to userid1
        for filename, (size, owner) in list(self.files.items()):
            if owner == userid2:
                self.files[filename] = (size, userid1)

        # Update userid1's capacity with userid2's capacity
        self.users[userid1] = total_capacity
        
        # Delete userid2
        del self.users[userid2]

        # Calculate and return remaining capacity
        remaining_capacity = total_capacity - (user1_used + user2_used)
        return str(remaining_capacity)

    def get_file_size(self, name: str) -> str:
        """Get file size if it exists."""
        return self.files[name][0] if name in self.files else ""

    def delete_file(self, name: str) -> str:
        """Delete file and return its size."""
        if name in self.files:
            return self.files.pop(name)[0]
        return ""

    def get_n_largest(self, prefix: str, n: int) -> str:
        """Get top N largest files with given prefix."""
        matching_files = [(name, int(size)) 
                         for name, (size, _) in self.files.items() 
                         if name.startswith(prefix)]
        
        if not matching_files:
            return ""
            
        matching_files.sort(key=lambda x: (-x[1], x[0]))
        result_files = matching_files[:n]
        formatted_files = [f"{name}({size})" for name, size in result_files]
        return ", ".join(formatted_files)
    

#level 4


    def backup_user(self, userid: str) -> str:
    
        if userid not in self.users:
            return ""
        
  
        user_files = {name: size for name, (size, owner) in self.files.items() 
                     if owner == userid}
        
        if not user_files:
            return "0"
            
        self.backups[userid] = user_files
        return str(len(user_files))

    def restore_user(self, userid: str) -> str:
     
        if userid not in self.users or userid not in self.backups:
            return ""
            
        backup = self.backups[userid]
        restored_count = 0
        
      
        current_files = [(name, size) for name, (size, owner) in self.files.items() 
                        if owner == userid]
        for name, _ in current_files:
            del self.files[name]
        
      
        for filename, size in backup.items():
          
            if filename in self.files:
                continue
            self.files[filename] = (size, userid)
            restored_count += 1
            
        return str(restored_count)
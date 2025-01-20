class InMemoryDb:
    def __init__(self):
        self.db = {}
        self.backups = []

    def SET(self, key, field, value):
        if key not in self.db:
            self.db[key] = {}
        self.db[key][field] = value
        return ""
    
    def GET(self, key, field):
        if key in self.db and field in self.db[key]:
            return self.db.get(key, {}).get(field, "")
        return ""
    
    def DELETE(self, key, field):
        if key in self.db and field in self.db[key]:
            del self.db[key][field]
            return "true"
        return "false"
    


    #level 2
    
    def SCAN(self, key):
        if key in self.db:
            sorted_fields = sorted(self.db[key].items())
            result = ','.join(f"{field}({value})" for field, value in sorted_fields)
            return result
        return ""
    def SCAN_BY_PREFIX(self, key, prefix):
        if key not in self.db:
            return ""
        fields = sorted(field for field in self.db[key].keys() if field.startswith(prefix) )
        return ','.join(f"{field}({self.db[key][field]})" for field in fields)
    



    #level 3

    def SET_AT(self, key: str, field: str, value: str, timestamp: int) -> str:
        """Sets a field-value pair at a specific timestamp."""
        if key not in self.db:
            self.db[key] = {}
        self.db[key][field] = {
            'value': value,
            'timestamp': timestamp,
            'ttl': None,
            'ttl_expiry': None
        }
        return ""
    

    def SET_AT_WITH_TTL(self, key, field, value, timestamp, ttl):
        if key not in self.db:
            self.db[key] = {}

        ttl_expiry = timestamp + ttl
        self.db[key][field] = {
            'value': value, 
            'timestamp': timestamp,
            'ttl': ttl,
            'ttl_expiry': timestamp + ttl
        }
        return ""


    def DELETE_AT(self, key: str, field: str, timestamp: int) -> str:
        """Deletes a field at a specific timestamp."""
        if key not in self.db or field not in self.db[key]:
            return "false"
        field_data = self.db[key][field]
        if field_data['ttl_expiry'] is not None and timestamp >= field_data['ttl_expiry']:
            return "false"
        del self.db[key][field]
        if not self.db[key]:
            del self.db[key]
        return "true"
        return 'false'
    

    def GET_AT(self, key: str, field: str, timestamp: int) -> str:
        """Gets the value of a field at a specific timestamp."""
        if key not in self.database or field not in self.db[key]:
            return ""
        field_data = self.db[key][field]
        if field_data['ttl_expiry'] is not None and timestamp >= field_data['ttl_expiry']:
            return ""
        return field_data['value']

    

    def SCAN_AT(self, key: str, timestamp: int) -> str:
        """Returns all valid fields at a specific timestamp."""
        if key not in self.db:
            return ""
        
        valid_fields = []
        for field, field_data in self.db[key].items():
            if field_data['ttl_expiry'] is None or timestamp < field_data['ttl_expiry']:
                valid_fields.append(f"{field}({field_data['value']})")
        
        return ", ".join(sorted(valid_fields))



    def SCAN_BY_PREFIX_AT(self, key, prefix, timestamp):
        self._clean_expired_fields
        if key in self.db:
            filetered_fields = {field: data for field, data in self.db[key].items() if field.startswith(prefix) and data['ttl_expiry'] is None or data['ttl_expiry'] > timestamp }
            if filetered_fields:
                sorted_fields = sorted(filetered_fields.items())
                result = ','.join(f"{field}({data['value']})" for field, data in sorted_fields)
                return result
        return ""
    



    #level 4
        
    def BACKUP(self, timestamp: int) -> str:
        """Creates a backup of the current database state."""
        # Deep copy the current database state
        backup_state = {}
        non_empty_records = 0
        
        for key, fields in self.db.items():
            backup_state[key] = {}
            has_valid_fields = False
            for field, data in fields.items():
                if data['ttl_expiry'] is None or timestamp < data['ttl_expiry']:
                    backup_state[key][field] = data.copy()
                    has_valid_fields = True
            if has_valid_fields:
                non_empty_records += 1
            if not backup_state[key]:
                del backup_state[key]
        
        self.backups.append((timestamp, backup_state))
        return str(non_empty_records)

#RESTORE <timestamp> <timestampToRestore>
    def RESTORE(self, timestamp: int, timestampToRestore: int) -> str:
        """Restores database from the latest backup before or at restore_point."""
        # Find the latest backup before or at restore_point
        valid_backups = [(t, state) for t, state in self.backups if t <= timestampToRestore]
        if not valid_backups:
            return ""
        
        backup_time, backup_state = max(valid_backups, key=lambda x: x[0])
        
        # Clear current database
        self.db = {}
        
        # Restore with recalculated TTLs
        for key, fields in backup_state.items():
            self.db[key] = {}
            for field, data in fields.items():
                new_data = data.copy()
                if data['ttl'] is not None:
                    # Calculate remaining TTL at backup time
                    elapsed_time = backup_time - data['timestamp']
                    remaining_ttl = data['ttl'] - elapsed_time
                    # Set new expiration time
                    new_data['timestamp'] = timestamp
                    new_data['ttl_expiry'] = timestamp + remaining_ttl
                self.db[key][field] = new_data
        
        return ""


            
        




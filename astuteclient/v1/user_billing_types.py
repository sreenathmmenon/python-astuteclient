from astuteclient.common import base

class UserBillingType(base.Resource):
    """
    """
    def __repr__(self):
        return "<UserBillingType %s>" % self._info

class UserBillingTypeManager(base.Manager):
    """
    """
    resource_class = UserBillingType
    
    def list(self):
        """
        List all user billing types
        """
        path = "/v1/billing/mapping"
        return self._list(path, "")
    
    
    def get(self, mapping_id):
        """
        Get the details of a specific user billing type mapping
        """
        path = "/v1/billing/mapping/" + mapping_id
        try:
            return self._list(path, expect_single=True)[0]
        except IndexError:
            return None
        
        
    def create(self, body):
        """
        Create a new user-billing type mapping
        """
        print('CREAAAAATE')
        print body
        print('==================')
        path = "/v1/billing/mapping"
        return self._create(path, body)
        
        
    def delete(self):
        """
        Delete a user-billing type mapping
        """
        
        
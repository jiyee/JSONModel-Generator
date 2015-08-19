NSSTRING_PROPERTY = "@property (nonatomic, strong) NSString *"
NSNUMBER_PROPERTY = "@property (nonatomic, strong) NSNumber *"
BOOL_PROPERTY     = "@property (nonatomic) BOOL "
NSSTRING          = "NSString"
NSNUMBER          = "NSNumber"
BOOL              = "BOOL"

PROPERTY_DECLARATIONS = {unicode: NSSTRING_PROPERTY, int: NSNUMBER_PROPERTY, bool: BOOL_PROPERTY}
APPLE_VAR_TYPES       = {unicode: NSSTRING, int: NSNUMBER, bool: BOOL}

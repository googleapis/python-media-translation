config = {
    "interfaces": {
        "google.cloud.mediatranslation.v1beta1.SpeechTranslationService": {
            "retry_codes": {"no_retry_codes": [], "no_retry_1_codes": []},
            "retry_params": {
                "no_retry_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 0,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 0,
                    "total_timeout_millis": 0,
                },
                "no_retry_1_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 400000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 400000,
                    "total_timeout_millis": 400000,
                },
            },
            "methods": {
                "StreamingTranslateSpeech": {
                    "timeout_millis": 355000,
                    "retry_codes_name": "no_retry_1_codes",
                    "retry_params_name": "no_retry_1_params",
                }
            },
        }
    }
}
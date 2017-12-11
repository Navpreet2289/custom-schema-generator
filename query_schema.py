class QuerySchema(AutoSchema):
    """
    This class provides an ability to specify extra query parameters in generated documentation
    """

    def get_link(self, path, method, base_url):
        link = super().get_link(path, method, base_url)

        return coreapi.Link(
            url=link.url,
            action=link.action,
            encoding=link.encoding,
            fields=link.fields + self.get_query_fields(path, method),
            description=link.description
        )

    def get_query_fields(self, path, method):
        return self.view.query_params if hasattr(self.view, 'query_params') else ()

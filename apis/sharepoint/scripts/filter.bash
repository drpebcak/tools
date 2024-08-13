# Thank you ChatGPT
yq eval '
    .paths |= with_entries(
      .value |= with_entries(
        select(
          ((.key == "get" or .key == "post" or .key == "put" or .key == "delete" or .key == "patch" or .key == "options" or .key == "head" or .key == "trace")
          and (
            .value.operationId == "sites.site.ListSite",
            .value.operationId == "sites.site.GetSite",
            .value.operationId == "sites.GetDrive",
            .value.operationId == "sites.ListDrives",
            .value.operationId == "sites.GetDrives",
            .value.operationId == "sites.drives.GetCount-5071",
            .value.operationId == "sites.ListItems",
            .value.operationId == "sites.GetItems",
            .value.operationId == "sites.items.GetCount-1b67",
            .value.operationId == "sites.ListLists",
            .value.operationId == "sites.GetLists",
            .value.operationId == "sites.lists.ListColumns",
            .value.operationId == "sites.lists.GetColumns",
            .value.operationId == "sites.lists.GetDrive",
            .value.operationId == "sites.lists.ListItems",
            .value.operationId == "sites.lists.GetItems",
            .value.operationId == "sites.lists.GetCount-e06a",
            .value.operationId == "sites.site.getByPath",
            .value.operationId == "sites.ListPages",
            .value.operationId == "sites.GetPages",
            .value.operationId == "sites.ListSites",
            .value.operationId == "sites.GetSites",
            .value.operationId == "sites.sites.GetCount-f499",
            .value.operationId == "sites.GetCount-6254",
            .value.operationId == "sites.getAllSites"
          )) or (.key == "description" or .key == "parameters")
        )
      )
    )
    | .paths |= with_entries(
      select(
        .value.get != null or .value.post != null or .value.put != null or .value.delete != null or .value.patch != null or .value.options != null or .value.head != null or .value.trace != null
      )
    )
  '


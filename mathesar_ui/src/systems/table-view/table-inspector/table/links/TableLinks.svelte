<script lang="ts">
  import { Spinner } from '@mathesar/component-library';
  import { getTabularDataStoreFromContext } from '@mathesar/stores/table-data';
  import { getJoinableTablesResult } from '@mathesar/stores/tables';
  import LinksSectionContainer from './LinksSectionContainer.svelte';
  import { getTableLinks } from './utils';

  const tabularData = getTabularDataStoreFromContext();

  $: tableId = $tabularData.id;
  $: columns = $tabularData.processedColumns;
</script>

<div>
  {#await getJoinableTablesResult(tableId)}
    <Spinner />
  {:then joinableTablesResult}
    <LinksSectionContainer
      linksInThisTable={getTableLinks(
        'in_this_table',
        joinableTablesResult,
        $columns,
      )}
      linksFromOtherTables={getTableLinks(
        'from_other_tables',
        joinableTablesResult,
        $columns,
      )}
    />
  {/await}
</div>
